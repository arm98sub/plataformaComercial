import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class GeneradorToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, usuario, timestamp):
        return six.text_type(usuario.id)+six.text_type(timestamp)+six.text_type(usuario.is_active)


token_activacion = GeneradorToken()
