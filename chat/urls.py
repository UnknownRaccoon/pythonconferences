from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^chat/$', views.MessageView.as_view(), name='chat_path'),
    url(r'^chat/$', views.MessageView.as_view(), name='chat_room'),
]
