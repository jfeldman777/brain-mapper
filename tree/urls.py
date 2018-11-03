from django.urls import path

from . import views

urlpatterns = [
    path('i_dir/', views.i_dir, name='i_dir'),
    path('i_tut/', views.i_tut, name='i_tut'),
    path('i_par/', views.i_par, name='i_par'),
    path('i_tea/', views.i_tea, name='i_tea'),
    path('i_stu/', views.i_stu, name='i_stu'),
    path('i_gue/', views.i_gue, name='i_gue'),
    path('i_adm/', views.i_adm, name='i_adm'),

    path('tree_nav/<int:id>/', views.tree_nav, name='tree_nav'),

    path('', views.index, name='index'),
]
