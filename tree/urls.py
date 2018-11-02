from django.conf.urls import url

from . import views

urlpatterns = [
    url('i_dir/', views.i_dir, name='i_dir'),
    url('i_tut/', views.i_tut, name='i_tut'),
    url('i_cur/', views.i_cur, name='i_cur'),
    url('i_par/', views.i_par, name='i_par'),
    url('i_tea/', views.i_tea, name='i_tea'),
    url('i_stu/', views.i_stu, name='i_stu'),
    url('i_gue/', views.i_gue, name='i_gue'),
    url('i_adm/', views.i_adm, name='i_adm'),

    url('', views.index, name='index'),
]
