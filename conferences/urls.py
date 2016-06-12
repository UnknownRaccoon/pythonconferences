from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='latest'),
    url(r'^(?P<pk>[0-9+])/$', views.ConferenceView.as_view(), name='conference_path'),
    url(r'^archive/$', views.ArchiveListView.as_view(), name='archive'),
    url(r'^(?P<conference>[0-9+])/support$', views.SupportView.as_view(), name='support_path'),
]
