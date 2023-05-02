from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config
import jwt
from .services.user_service import UserService

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    accessToken = refresh.access_token

    encoded = insert_claims(accessToken, user.get_username(), user.get_email())

    return {
        'refresh': str(refresh),
        'access_token': str(encoded),
    }
    
def remove_tokens(refresh_token):
    try:
        refresh = RefreshToken(refresh_token)
        refresh.blacklist()
        return True
    except:
        return False
    
def refresh_token(refresh_token):
    try:
        refresh = RefreshToken(refresh_token)
        accessToken = refresh.access_token

        userService = UserService()
        user = userService.get_by_id(refresh['user_id'])

        encoded = insert_claims(accessToken, user.get_username(), user.get_email())
        return {
            'refresh': str(refresh),
            'access_token': str(encoded),
            }
    except:
        return None
    
def insert_claims(accessToken, username, email):
    decodeJTW = jwt.decode(str(accessToken), config('SECRET_KEY'), algorithms=["HS256"])
    # add payload here!!
    decodeJTW['username'] = username
    decodeJTW['email'] = email
    encoded = jwt.encode(decodeJTW, config('SECRET_KEY'), algorithm="HS256")
    return encoded