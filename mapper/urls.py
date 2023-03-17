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
from django.urls import include, path

from tree import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = []

if settings.DEBUG:#в этом режиме медиафайлы берутся из статической папки MEDIA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('kid2parent/', views.kid2parent, name='kid2parent'),
    path('kid2teacher/', views.kid2teacher, name='kid2teacher'),
    path('register_adm/', views.register_adm, name='register_adm'),
    path('register_dir/', views.register_dir, name='register_dir'),
    path('register_tut/', views.register_tut, name='register_tut'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('i_dir/', views.i_dir, name='i_dir'),
    path('i_tut/', views.i_tut, name='i_tut'),
    path('i_par/', views.i_par, name='i_par'),
    path('i_tea/', views.i_tea, name='i_tea'),
    path('i_stu/', views.i_stu, name='i_stu'),
    path('i_gue/', views.i_gue, name='i_gue'),
    path('i_adm/', views.i_adm, name='i_adm'),
    path('', include('tree.urls')),
]
