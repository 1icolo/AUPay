from hashlib import sha256


def hash(text: str):
    try:
        return sha256(text.encode()).hexdigest()
    except:
        return None


def verify(hashed_text, text):
    text = hash(text)
    if hashed_text == text.hexdigest():
        return True
    return False