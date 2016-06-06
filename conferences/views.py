from datetime import datetime, timedelta
from django.views import generic
from django.views.generic import edit
from .models import Conference, Profile, Article
from django.contrib.auth.models import User
from . import forms


class IndexView(generic.ListView):
    template_name = 'conferences/index.html'
    context_object_name = 'conferences'

    def get_queryset(self):
        return Conference.objects.order_by('-date').filter(date__gte=(datetime.now() - timedelta(days=3)))


class ConferenceView(generic.DetailView):
    model = Conference
    template_name = 'conferences/conference.html'

    def get_context_data(self, **kwargs):
        context = super(ConferenceView,self).get_context_data(**kwargs)
        context['registration_form'] = forms.RegistrationForm
        return context


class SignupView(edit.CreateView):
    template_name = 'registration/register.html'
    model = User
    fields = ['email', 'username', 'password']
    success_url = '/account'


class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_queryset(self):
        return Profile.objects.filter(user_id=self.request.user.id).first()


class ArticlesView(generic.ListView):
    paginate_by = 5
    model = Article
    template_name = 'articles/index.html'


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'articles/article.html'