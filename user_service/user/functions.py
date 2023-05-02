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

        encoded = jwt.encode(decodeJTW, config('SECRET_KEY'), algorithm="HS256")

        return {
            'refresh': str(refresh),
            'access': str(encoded),
        }
            return encoded