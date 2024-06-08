import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model


User = get_user_model()


class UserAuthentication(BaseAuthentication):
    """handle authentication for user"""

    def authenticate(self, request):
        """authenticate user"""

        token = self.extract_token(request)
        if token is None:
            return None

        try:
            payload = jwt.decode(token, key=settings.SECRET_KEY, algorithms=['HS256'])
            self.verify_payload(payload)
            user = User.objects.get(id=payload.get("id"))
            return user
        except (InvalidTokenError, ExpiredSignatureError, User.DoesNotExist):
            raise AuthenticationFailed("Invalid Token")

    def verify_payload(self, payload):
        """verify token expiration"""
        if not "exp" in payload:
            raise InvalidTokenError("Token has no Expiration")
        
        exp_timestamp = payload["exp"]
        current_timestamp = datetime.now().timestamp()
        
        if current_timestamp > exp_timestamp:
            raise ExpiredSignatureError("Token is expired")

    def extract_token(self, request):
        """extract token from header"""

        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            return auth_header.split(" ")[1]
        return None

    @staticmethod
    def encrypt_payload(payload: dict) -> dict:
        """encrypt users information"""

        exp = datetime.now() + timedelta(hours=24)
        payload['exp'] = exp
        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')
        return token
