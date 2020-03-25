"""my_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.urls import include, path
from . import views

app_name = 'main'
urlpatterns = [
    path('clients/', include('clients.urls')),
    path('', views.Index.as_view(), name='index'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('auth/loging', views.Login.as_view()),
    path('auth/logout', views.Logout.as_view()),
    path('api/item', views.Item.as_view()),
    url(r'^admin/', admin.site.urls),
]