from django.urls import path

from . import views, v_cur

urlpatterns = [
    path('move_item/<int:id>/', v_cur.move_item),
    path('add_item/<int:id>/<int:location>/', v_cur.add_item),
    path('subtree/<int:id>/', v_cur.subtree, name='subtree'),
    path('tree_nav/<int:id>/', views.tree_nav, name='tree_nav'),
    path('change_txt/<int:id>/', v_cur.change_txt, name='change_txt'),
    path('change_figure/<int:id>/', v_cur.change_figure, name='change_figure'),

    path('', views.index, name='index'),
]
