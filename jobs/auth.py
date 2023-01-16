#!/usr/bin/env python3

from django.contrib.auth.backends import BaseBackend

class SupaAuthBackend:
    def authenticate(self, request, token=None):
        # validate jwt
        # extract id
        try:
            user = services.find_user_by_email(email=email)
        except Http404:
            return None

        return user if user.check_password(password) else None

    def get_user(self, user_id):
        # Parse token here to get user id
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
