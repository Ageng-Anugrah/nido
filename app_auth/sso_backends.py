from django_cas_ng.backends import CASBackend
from django_cas_ng.signals import cas_user_authenticated
from django_cas_ng.utils import get_cas_client
from django.conf import settings

from django.contrib.auth import get_user_model

from app_profile.models import UserProfile
from app_auth.utils import (
    get_additional_data,
    get_generation_by_npm
)


class SSOCASBackend(CASBackend):
    def authenticate(self, request, ticket, service):
        """Verifies CAS ticket and gets or creates User object"""
        client = get_cas_client(service_url=service, request=request)
        username, attributes, pgtiou = client.verify_ticket(ticket)
        user_model = get_user_model()
        if attributes and request:
            request.session['attributes'] = attributes
        if not username:
            return None

        user, created = user_model.objects.get_or_create(
            username=username.lower(),
        )
        # Two "if" under this line is added because there was some troubles in SSO so the retrieved data is not same as usual.
        if "npm" in attributes:
            user.npm = attributes["npm"]
            user.generation = get_generation_by_npm(attributes["npm"])
        if "nama" in attributes:
            user.name = attributes["nama"]
        user.save()

        UserProfile.objects.get_or_create(
            id=user.id,
            user=user
        )

        if not settings.CAS_SERVER == 'CAS 3' and 'kd_org' in attributes:
            additional_data = get_additional_data(attributes['kd_org'])
            if additional_data:
                user.faculty = additional_data['faculty']
                user.study_program = additional_data['study_program']
                user.educational_program = additional_data['educational_program']
                user.save()

        # send the `cas_user_authenticated` signal
        cas_user_authenticated.send(
            sender=self,
            user=user,
            created=created,
            attributes=attributes,
            ticket=ticket,
            service=service,
            request=request
        )
        return user
