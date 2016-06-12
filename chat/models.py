
from django.db import models
from custom_auth.models import Profile


class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name='sender')
    recipient = models.ForeignKey(Profile, related_name='recipient')
    text = models.TextField()
    date = models.DateTimeField()

    def as_dict(self):
        return {'sender': self.sender.id, 'recipient': self.recipient.id, 'text': self.text, 'date': str(self.date)}