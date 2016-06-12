from django.conf.urls import include, url
from custom_auth.views import SignupView
from conferences.views import IndexView
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
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

# The only easy way to make email unique
User._meta.get_field_by_name('email')[0]._unique = True

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='root'),
    url(r'^conferences/', include('conferences.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', SignupView.as_view(), name='signup'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^', include('custom_auth.urls')),
    url(r'^', include('chat.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
