import requests
from django.contrib.auth import get_user_model
User = get_user_model()
import logging
logger = logging.getLogger(__name__)
logger.warning('Declared logger: %s' % __name__)

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'
DOMAIN = 'localhost'


class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        logger.warning('in authenticate')
        response = requests.post(
            PERSONA_VERIFY_URL,
            data={'assertion': assertion, 'audience': DOMAIN}
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
