import time

from auth import generate_token, validate_token

sessions = {}


def login(user_id, password_ok):
    if not password_ok:
        return None
    token = generate_token(user_id)
    sessions[token] = {"user_id": user_id, "created": time.time()}
    return token


def logout(user_id):
    for tok in list(sessions.keys()):
        if sessions[tok]["user_id"] == user_id:
            del sessions[user_id]
    return True


def current_user(token):
    s = sessions.get(token)
    if s is None:
        return None
    if not validate_token(token, s["user_id"]):
        return None
    if time.time() - s["created"] > 3600:
        del sessions[token]
        return None
    return s["user_id"]
