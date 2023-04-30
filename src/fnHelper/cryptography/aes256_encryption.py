from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
import binascii

def encrypt(encryption_text: str, secret_key: str, initial_vector: str = "Shine On, Dear AUP!") -> str:
    # Define a salt value for the key derivation function
    salt = b'\x00' * 16
    
    # Derive a fixed-length key from the input secret key using PBKDF2
    derived_key = PBKDF2(secret_key, salt, dkLen=32)
    
    # Derive a fixed-length initial vector from the input initial vector using SHA256
    derived_iv = SHA256.new(initial_vector.encode('utf-8')).digest()[:16]
    
    # Create a new AES cipher object in CBC mode using the derived key and derived initial vector
    cipher = AES.new(derived_key, AES.MODE_CBC, derived_iv)
    
    # Pad the input text to be encrypted using PKCS7 padding
    padded_data = pad(encryption_text.encode('utf-8'), AES.block_size)
    
    # Encrypt the padded data using the AES cipher object
    encrypted_text = cipher.encrypt(padded_data)
    
    # Convert the encrypted data to a hexadecimal string and return it as the result of the function
    return binascii.hexlify(encrypted_text).decode('utf-8')

def decrypt(encryption_text: str, secret_key: str, initial_vector: str = "Shine On, Dear AUP!") -> str:
    # Define a salt value for the key derivation function
    salt = b'\x00' * 16
    
    # Derive a fixed-length key from the input secret key using PBKDF2
    derived_key = PBKDF2(secret_key, salt, dkLen=32)
    
    # Derive a fixed-length initial vector from the input initial vector using SHA256
    derived_iv = SHA256.new(initial_vector.encode('utf-8')).digest()[:16]
    
    # Create a new AES cipher object in CBC mode using the derived key and derived initial vector
    cipher = AES.new(derived_key, AES.MODE_CBC, derived_iv)
    
    # Convert the input text from a hexadecimal string to binary data
    encrypted_text = binascii.unhexlify(encryption_text)
    
    # Decrypt the encrypted data using the AES cipher object
    decrypted_text = unpad(cipher.decrypt(encrypted_text), AES.block_size)
    
    # Remove any padding added during encryption and return the decrypted text as a string
    return decrypted_text.decode('utf-8')