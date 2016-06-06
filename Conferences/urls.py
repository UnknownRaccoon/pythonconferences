from django.conf.urls import include
from conferences import views

"""Conferences URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User

# The only easy way to make email unique
User._meta.get_field_by_name('email')[0]._unique = True

urlpatterns = [
    url(r'^', include('conferences.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', views.SignupView.as_view(), name='signup'),
    url(r'^', include('django.contrib.auth.urls')),
]
