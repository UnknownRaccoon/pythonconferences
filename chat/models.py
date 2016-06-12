
from django.db import models
from custom_auth.models import Profile


class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name='sender')
    recipient = models.ForeignKey(Profile, related_name='recipient')
    text = models.TextField()
    date = models.DateTimeField()

    def as_dict(self):
        return {'sender': self.sender.user.username, 'recipient': self.recipient.user.username, 'text': self.text, 'date': str(self.date)}

    def __repr__(self):
        return "Sender: {}, recipient: {}, message: {}".format(self.sender.user.username, self.recipient.user.username,
                                                               self.text[:100] + '...')
