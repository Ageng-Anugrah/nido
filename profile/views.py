from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from rest_framework_jwt.settings import api_settings
from profile.forms import ProfileForm
from django.urls import reverse
from django.shortcuts import redirect

from app_auth.models import User
from app_profile.models import UserProfile

from django.http import HttpResponseRedirect
from django_cas_ng.utils import get_cas_client, get_service_url

from app_auth.utils import get_login_redirect_url

# Create your views here.


def is_profile_filled(user_profile):
    if (user_profile.phone_number == None or
        user_profile.secondary_email == None or
            user_profile.line_id == None):
        return False
    return True


@csrf_exempt
@require_http_methods(["GET", "POST"])
def forms_page_token_views(request,):
    next_page = request.GET.get('next_page', None)
    token = request.GET.get('token', None)
    # TODO: Add logic from POST request logic
    response = {}

    jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
    user_data = jwt_decode_handler(token)
    user = User.objects.get(npm=user_data['npm'])
    user_profile = UserProfile.objects.get(user=user)

    update_user_profile, _ = UserProfile.objects.get_or_create(user=user)

    is_user_profile_filled = is_profile_filled(update_user_profile)

    initial_form_value = {}
    # initial_form_value['photo'] = update_user_profile.photo
    initial_form_value['phone_number'] = update_user_profile.phone_number
    initial_form_value['secondary_email'] = update_user_profile.secondary_email
    initial_form_value['line_id'] = update_user_profile.line_id
    initial_form_value['birth_place'] = update_user_profile.birth_place
    if update_user_profile.birth_date:
        birth_date = ('%s-%s-%s') % (update_user_profile.birth_date.year,
                                     update_user_profile.birth_date.month, update_user_profile.birth_date.day)
        initial_form_value['birth_date'] = birth_date
    initial_form_value['home_address'] = update_user_profile.home_address
    initial_form_value['current_address'] = update_user_profile.current_address

    response['profile_form'] = ProfileForm(initial=initial_form_value)
    response['next_page'] = next_page
    response['token'] = token
    response['user_created'] = is_user_profile_filled

    response['form_action'] = reverse(
        'profile:post-profile') + '?next_page=' + response['next_page'] + '&token=' + response['token']

    return render(request, 'forms.html', response)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def profile_post_views(request):
    next_page = request.GET.get('next_page', None)
    token = request.GET.get('token', None)
    response = {}
    response['profile_form'] = ProfileForm
    response['next_page'] = next_page
    response['token'] = token
    response['form_action'] = reverse(
        'profile:post-profile') + '?next_page=' + response['next_page'] + '&token=' + response['token']

    form = ProfileForm(request.POST or None)
    if(form.is_valid()):

        jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
        user_data = jwt_decode_handler(token)
        user = User.objects.get(npm=user_data['npm'])
        user_profile = UserProfile.objects.get(user=user)

        update_user_profile, _ = UserProfile.objects.get_or_create(user=user)

        if (request.POST['birth_date_day'] == request.POST['birth_date_month'] ==
                request.POST['birth_date_year'] == '0'):
            birth_date = None
        else:
            birth_date = ('%s-%s-%s') % (request.POST['birth_date_year'],
                                         request.POST['birth_date_month'], request.POST['birth_date_day'])

        # update_user_profile.photo = request.POST['photo']
        update_user_profile.phone_number = request.POST['phone_number']
        update_user_profile.secondary_email = request.POST['secondary_email']
        update_user_profile.line_id = request.POST['line_id']
        update_user_profile.birth_place = request.POST['birth_place']
        update_user_profile.birth_date = birth_date
        update_user_profile.home_address = request.POST['home_address']
        update_user_profile.current_address = request.POST['current_address']

        update_user_profile.save()

        if 'https://' not in next_page:
            next_page = 'https://' + next_page
        next_page = get_login_redirect_url(request.user, next_page)
        return HttpResponseRedirect(next_page)
    else:
        return render(request, 'forms.html', response)
