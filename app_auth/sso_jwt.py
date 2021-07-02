from datetime import datetime
from calendar import timegm
from rest_framework_jwt.settings import api_settings

from app_profile.models import UserProfile

def jwt_payload_handler(user):
    """ Custom payload handler
    Token encrypts the dictionary returned by this function, and can be decoded by rest_framework_jwt.utils.jwt_decode_handler
    """
    user_profile, _ = UserProfile.objects.get_or_create(user=user)
    try:
        return {
            'user_id': user.pk,
            'name': user.name,
            'username': user.username,
            'npm': user.npm,
            'is_superuser': user.is_superuser,
            'phone_number': user_profile.phone_number,
            'email': user_profile.secondary_email,
            'line_id': user_profile.line_id,
            'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
            'orig_iat': timegm(
                datetime.utcnow().utctimetuple()
            )
        }
    except Exception:
        return {
            'user_id': user.pk,
            'username': user.username,
            'is_superuser': user.is_superuser,
            'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
            'orig_iat': timegm(
                datetime.utcnow().utctimetuple()
            )
        }



def jwt_response_payload_handler(token, user=None, request=None):
    """ Custom response payload handler.

    This function controlls the custom payload after login or token refresh. This data is returned through the web API.
    """
    return {
        'token': token,
        'user': {
            'username': user.username,

        }
    }
