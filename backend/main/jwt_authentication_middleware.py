import jwt
from django.contrib.auth.models import User
from django.http import JsonResponse

from common_utils import get_env_key

JWT_SECRET_KEY = get_env_key('JWT_SECRET_KEY')


# our custom function to handle JWT authentication of requests as part of the middleware
# this is included in the settings.py file
class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        # print(":::JWT authentication:::")
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get('Authorization', None)
        if token:
            try:
                payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
                user = User.objects.get(id=payload['user_id'])
                # print(":::JWT auth get by user id:::")
                request.user = user
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist) as e:
                print(f"Exception {e}")
                return JsonResponse({'error': 'Invalid token'}, status=401)
        else:
            request.user = None
        return self.get_response(request)
