from datetime import datetime, timedelta
from custom_auth.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Conference, Participation
from . import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import pytz


class IndexView(generic.ListView):
    template_name = 'conferences/index.html'
    context_object_name = 'conferences'

    def get_queryset(self):
        return Conference.objects.order_by('-date').filter(date__gte=(datetime.now() - timedelta(days=3)))


class ArchiveListView(LoginRequiredMixin, generic.ListView):
    template_name = 'conferences/index.html'
    context_object_name = 'conferences'

    def get_queryset(self):
        return Conference.objects.order_by('-date').filter(date__lt=(datetime.now() - timedelta(days=3)))


class ConferenceView(LoginRequiredMixin, generic.DetailView):
    model = Conference
    template_name = 'conferences/conference.html'

    def post(self, request, *args, **kwargs):
        Participation.objects.create(profile=request.user.profile,
                                     conference=self.get_object(), role=request.POST['role'],
                                     subject=request.POST['subject'],
                                     description=request.POST['about'])
        return HttpResponseRedirect(reverse('conference_path', args=[self.get_object().id]))

    def get_context_data(self, **kwargs):
        context = super(ConferenceView, self).get_context_data(**kwargs)
        context['registration_form'] = forms.RegistrationForm
        context['speakers'] = Participation.objects.filter(role=True, conference__id=self.kwargs['pk'])
        if pytz.utc.localize(datetime.now()) > self.get_object().date:
            context['participants'] = Profile.objects.filter(conference=self.get_object())
        return context


class SupportView(LoginRequiredMixin, generic.View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.company is not None:
            Conference.objects.get(pk=kwargs['conference']).companies.add(request.user.company)
        return HttpResponseRedirect(reverse('conference_path', args=[kwargs['conference']]))
