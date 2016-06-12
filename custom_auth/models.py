from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.name


class Profile(models.Model):
    company = models.ForeignKey(Company, null=True, blank=True)
    user = models.OneToOneField(User)
    avatar = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username
