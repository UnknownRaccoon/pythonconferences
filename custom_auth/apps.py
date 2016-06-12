from django.apps import AppConfig
from django.db.models.signals import post_save


class AuthConfig(AppConfig):
    name = 'custom_auth'

    def ready(self):
        from django.contrib.auth.models import User
        from .models import Company, Profile
        from .signals import create_profile, save_company, save_profile
        post_save.connect(create_profile, sender=User)
        post_save.connect(save_company, sender=Company)
        post_save.connect(save_profile, sender=Profile)
