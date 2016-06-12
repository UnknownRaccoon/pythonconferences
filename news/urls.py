from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.ArticlesView.as_view(), name='articles'),
    url(r'^(?P<pk>[0-9+])/$', views.ArticleView.as_view(), name='article_path'),
]
