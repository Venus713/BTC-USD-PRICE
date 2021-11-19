from django.conf import settings
from rest_framework.permissions import BasePermission


class ApiKeyAuth(BasePermission):
    def has_permission(self, request, view):
        # API_KEY should be in request headers to authenticate requests
        api_key_secret = request.headers.get("API_KEY")
        return api_key_secret == settings.API_KEY_SECRET
