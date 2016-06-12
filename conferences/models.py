from django.db import models
from django.contrib.auth.models import User
from custom_auth.models import Profile, Company


class Conference(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    participants = models.ManyToManyField(Profile, through='Participation')
    companies = models.ManyToManyField(Company, blank=True)

    def __str__(self):
        return self.name


class Participation(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    role = models.BooleanField()
    subject = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    @classmethod
    def participants_info(cls, profile, ):
        return cls.objects.filter()
