from app.models import UserModel
from app import bcrypt



def authenticate(email, password):
    user = UserModel.get_by_email(email)
    if user and bcrypt.check_password_hash(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.get_by_id(user_id)
