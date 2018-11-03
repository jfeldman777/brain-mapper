from django.urls import path

from . import views, v_cur

urlpatterns = [
    path('tree_nav/<int:id>/', views.tree_nav, name='tree_nav'),
    path('change_txt/<int:id>/', v_cur.change_txt, name='change_txt'),
    path('change_figure/<int:id>/', v_cur.change_figure, name='change_figure'),

    path('', views.index, name='index'),
]
