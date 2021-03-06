import requests
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'


class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        response = requests.post(
            PERSONA_VERIFY_URL,
            data={'assertion': assertion, 'audience': settings.DOMAIN}
        )

        if response.ok and response.json()['status'] == 'okay':
            try:
                return User.objects.get(email=response.json()['email'])
            except:
                return User.objects.create(email=response.json()['email'])

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
