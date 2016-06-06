from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField()


class Profile(models.Model):
    company = models.ForeignKey(Company,null=True)
    user = models.OneToOneField(User)
    avatar = models.ImageField()

    def __str__(self):
        return self.user.username


class Conference(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    participants = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_published = models.DateTimeField()


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        up = Profile(user=user)
        up.save()

post_save.connect(create_profile, sender=User)