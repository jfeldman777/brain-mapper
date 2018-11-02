"""mapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url

from tree import views

urlpatterns = [
    url('register_adm/', views.register_adm, name='register_adm'),
    url('register_dir/', views.register_dir, name='register_dir'),
    url('register_tut/', views.register_tut, name='register_tut'),

    url('accounts/', include('django.contrib.auth.urls')),

    url('admin/', admin.site.urls),
    url('', include('tree.urls')),
]
