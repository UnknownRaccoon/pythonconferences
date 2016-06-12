from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import edit
from django.views import generic
from .models import Message
from custom_auth.models import Profile


class MessageView(LoginRequiredMixin, edit.CreateView):
    template_name = 'messages/message.html'
    model = Message
    fields = ['text']

    def get_context_data(self, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)
        context['previous_messages'] =\
            (Message.objects.filter(recipient=self.request.user.profile, sender__id=self.request.GET['companion']) |
             Message.objects.filter(sender=self.request.user.profile, recipient__id=self.request.GET['companion']))
        context['companion'] = Profile.objects.get(user__id=self.request.GET['companion'])
        return context

    def dispatch(self, request, *args, **kwargs):
        if 'companion' in self.request.GET:
            return super(MessageView, self).dispatch(request, *args, **kwargs)
        return ChatListView.as_view()(request)


class ChatListView(LoginRequiredMixin, generic.ListView):
    template_name = 'messages/chats.html'

    def get_queryset(self):
        q = (Message.objects.filter(recipient=self.request.user.profile) |
             Message.objects.filter(sender=self.request.user.profile)).\
            distinct('sender').distinct('recipient')
        return q
