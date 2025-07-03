# users/users.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("admin123"),
        "disabled": False
    }
}

def get_user(username: str):
    user = fake_users_db.get(username)
    if user:
        return user
