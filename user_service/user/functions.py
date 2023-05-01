from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config
import jwt

class Functions:

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        accessToken = refresh.access_token

        decodeJTW = jwt.decode(str(accessToken), config('SECRET_KEY'), algorithms=["HS256"])

        # add payload here!!
        decodeJTW['username'] = user.username
        decodeJTW['email'] = user.email

        encoded = jwt.encode(decodeJTW, config('SECRET_KEY'), algorithm="HS256")

        return {
            'refresh': str(refresh),
            'access': str(encoded),
        }
        