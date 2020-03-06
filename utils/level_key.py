import hashlib

def get_hash(key: str):
    return hashlib.sha384(key.encode()).digest().hex()[:10]