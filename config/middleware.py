from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/graphql'):
            auth = JWTAuthentication()
            try:
                user_auth_tuple = auth.authenticate(request)
                if user_auth_tuple is not None:
                    request.user = user_auth_tuple[0]
            except (InvalidToken, AuthenticationFailed):
                pass
