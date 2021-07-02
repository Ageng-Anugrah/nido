import json
import os

from rest_framework_jwt.settings import api_settings
from django.conf import settings

module_dir = os.path.dirname(__file__)  # get current directory


def get_generation_by_npm(npm):
    try:
        return int('20{}'.format(npm[0:2]))
    except Exception:
        return 0


def get_additional_data(id):
    file_path = os.path.join(module_dir, 'additional_data.json')
    try:
        with open(file_path) as f:
            data = json.load(f)
            return data[id]
    except Exception:
        return None


def get_login_redirect_url(user, url):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    jwt_payload = jwt_payload_handler(user)
    jwt_token = jwt_encode_handler(jwt_payload)

    # url = settings.CAS_REDIRECT_URL

    return '{}?token={}'.format(url, jwt_token)


def get_jwt_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    jwt_payload = jwt_payload_handler(user)
    jwt_token = jwt_encode_handler(jwt_payload)

    return jwt_token

def get_jwt_token_simple(user):
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    jwt_payload = {
        'npm': user.npm,
    }
    jwt_token = jwt_encode_handler(jwt_payload)

    return jwt_token


def get_logout_redirect_url():
    url = settings.CLIENT_HOST

    return '{}'.format(url)
