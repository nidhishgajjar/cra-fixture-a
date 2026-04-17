import hashlib
import secrets

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password, stored_hash):
    return hash_password(password) == stored_hash


def generate_token(user_id):
    return f"{user_id}-{secrets.token_hex(16)}"


def validate_token(token, user_id):
    return token.startswith(f"{user_id}-") and len(token) == len(f"{user_id}-") + 32
