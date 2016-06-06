from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='latest'),
    url(r'^conferences/(?P<pk>[0-9+])/$', views.ConferenceView.as_view(), name='conference_path'),
    url(r'^account/$', views.ProfileView.as_view(), name='profile_path'),
    url(r'^news/$', views.ArticlesView.as_view(), name='articles'),
    url(r'^news/(?P<pk>[0-9+])/$', views.ArticleView.as_view(), name='article_path'),
]
