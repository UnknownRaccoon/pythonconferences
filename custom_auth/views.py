from custom_auth.forms import UpdateProfileForm, UpdateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.views import generic
from django.views.generic import edit
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from .models import Profile


class SignupView(edit.CreateView):
    template_name = 'registration/register.html'
    model = User
    fields = ['email', 'username', 'password']

    def get_success_url(self):
        return reverse('profile_path', args=[self.object.id])

    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        form.instance.save()
        return super(SignupView, self).form_valid(form)


class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile.html'


class ProfileUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'registration/update.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['profile_form'] = UpdateProfileForm(instance=self.request.user.profile)
        context['user_form'] = UpdateUserForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        print(request.FILES)
        profile_form = UpdateProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        user_form = UpdateUserForm(data=request.POST, files=request.FILES, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
        print(profile_form.errors.keys())
        print(user_form.errors.keys())
        return HttpResponseRedirect(reverse('profile_path', args=[self.request.user.id]))

class AddProfileToCompanyView(generic.View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.company is not None:
            request.user.company.profile_set.add(Profile.objects.get(pk=kwargs['profile']))
        return HttpResponseRedirect(reverse('profile_path', args=[kwargs['profile']]))