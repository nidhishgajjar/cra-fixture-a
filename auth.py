import hashlib
import secrets

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(password, stored_hash):
    return hash_password(password) == stored_hash


def generate_token(user_id):
    raw = f"{user_id}-{secrets.token_hex(8)}"
    return raw


def validate_token(token, user_id):
    return token.startswith(f"{user_id}-")
