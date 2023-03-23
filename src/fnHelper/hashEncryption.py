from hashlib import sha256


def encrypt(text: str):
    return sha256(text.encode()).hexdigest()


def verify(hash, text):
    text = encrypt(text)
    if hash == text.hexdigest():
        return True
    return False