from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^accounts/(?P<pk>[0-9+])/$', views.ProfileView.as_view(), name='profile_path'),
    url(r'^accounts/(?P<pk>[0-9+])/update/$', views.ProfileUpdateView.as_view(), name='edit_profile_path'),
    url(r'^accounts/(?P<profile>[0-9+])/invite/$', views.AddProfileToCompanyView.as_view(), name='invite_path'),
]
