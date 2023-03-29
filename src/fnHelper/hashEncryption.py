from hashlib import sha256


def encrypt(text: str):
    try:
        return sha256(text.encode()).hexdigest()
    except:
        return None


def verify(hash, text):
    text = encrypt(text)
    if hash == text.hexdigest():
        return True
    return False