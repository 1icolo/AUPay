from hashlib import sha256

def hash(text: str):
    try:
        return sha256(text.encode()).hexdigest()
    except Exception as e:
        pass

def verify(hashed_text, text: str):
    if hashed_text == sha256(text.encode()).hexdigest():
        return True
    return False