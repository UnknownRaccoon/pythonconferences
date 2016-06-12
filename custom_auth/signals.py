from .models import Profile
from PIL import Image
from django.conf import settings


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        Profile.objects.create(user=user)


def save_profile(sender, **kwargs):
    profile = kwargs["instance"]
    if profile.avatar is not None and profile.avatar != '' and (profile.avatar.width > 128 or profile.avatar.height > 128):
        full_path = settings.MEDIA_ROOT+(profile.avatar.name[1:])
        image = Image.open(full_path)
        image.thumbnail((128, 128), Image.ANTIALIAS)
        image.save(full_path)
        image.close()


def save_company(sender, **kwargs):
    company = kwargs["instance"]
    if company.logo is not None and (company.logo.width > 128 or company.logo.height > 128):
        full_path = settings.MEDIA_ROOT+(company.logo.name[1:])
        image = Image.open(full_path)
        image.thumbnail((128, 128), Image.ANTIALIAS)
        image.save(full_path)
        image.close()
