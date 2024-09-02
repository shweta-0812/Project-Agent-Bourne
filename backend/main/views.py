# views.py

import json
import requests
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from user.service.user_service import get_or_create_new_individual_user, update_user_last_login
from dotenv import load_dotenv, find_dotenv
from common_utils import get_env_key
from user.models.user_detail_model import UserTypes
import datetime
import jwt


_ = load_dotenv(find_dotenv())  # read local .env file

# all the info including Redirect URI should be same as used in frontend
GOOGLE_CLIENT_ID = get_env_key('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = get_env_key('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = get_env_key('GOOGLE_REDIRECT_URI')
GOOGLE_TOKEN_URL = get_env_key('GOOGLE_TOKEN_URL')
JWT_SECRET_KEY = get_env_key('JWT_SECRET_KEY')


def generate_jwt_token(user_data: dict) -> str:
    payload = {**user_data,
               'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
               'iat': datetime.datetime.utcnow()}
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return token


@csrf_exempt
@ensure_csrf_cookie
def google_callback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')

        token_url = GOOGLE_TOKEN_URL
        token_data = {
            'code': code,
            'client_id': GOOGLE_CLIENT_ID,
            'client_secret': GOOGLE_CLIENT_SECRET,
            'redirect_uri': GOOGLE_REDIRECT_URI,
            'grant_type': 'authorization_code',
        }

        token_response = requests.post(token_url, data=token_data)
        token_info = token_response.json()
        if 'error' in token_info:
            return JsonResponse({'error': token_info['error']}, status=400)

        # Verify the token
        id_info = id_token.verify_oauth2_token(token_info['id_token'], google_requests.Request(), GOOGLE_CLIENT_ID)

        # use user data to get existing user or create new user
        user_detail = get_or_create_new_individual_user(user_data={
            'email': id_info['email'],
            'name': id_info['name'],
            'is_admin': True,
            'profile_pic_url': id_info['picture'],
            'oauth_provider': 'google',
            'oauth_id': id_info['sub'],
            'user_type': UserTypes.INDIVIDUAL
        })
        update_user_last_login(user_id=user_detail['id'])
        # Send user data back to the frontend
        # user_data = {
        #     'user_id': user_detail.id,
        #     'google_id': id_info['sub'],
        #     'email': id_info['email'],
        #     'name': id_info['name'],
        #     'picture': id_info['picture'],
        # }
        user_data = {
            'user_id': user_detail['id'],
            'oauth_provider': user_detail['oauth_provider'],
            'oauth_id': user_detail['oauth_id'],
            'email': user_detail['email'],
            'name': user_detail['name'],
            'profile_pic_url': user_detail['profile_pic_url'],
            'user_type': user_detail['user_type'],
            'is_admin': user_detail['is_admin'],
        }
        # we can use access_token to access other google info for the user
        # we can use refresh token to get new access token once the current token expires
        # generate a JWT token
        jwt_token = generate_jwt_token(user_data)
        user_data["jwt_token"] = jwt_token
        return JsonResponse(user_data)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


# Django automatically sets a CSRF token for each user session. You can access this token and send it to the frontend
# through a view.
@ensure_csrf_cookie
def get_csrf_token(request):
    # CSRF token is set in the cookie by ensure_csrf_cookie decorator
    return JsonResponse({'csrftoken': 'success'})
