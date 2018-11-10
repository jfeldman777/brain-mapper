from django.urls import path

from . import views, v_cur

urlpatterns = [
    path('see_us/<slug:type>/', views.see_us),
    path('topic_search/', views.topic_search),
    path('exam/<int:id>/', v_cur.exam),
    path('q_edit/<int:id>/', v_cur.q_edit),
    path('q_delete/<int:id>/', v_cur.q_delete),
    path('q_add/<int:id>/', v_cur.q_add),
    path('q_figure/<int:id>/', v_cur.q_figure),
    path('q_list/<int:id>/', v_cur.q_list),
    path('move_item/<int:id>/', v_cur.move_item),
    path('add_item/<int:id>/<int:location>/', v_cur.add_item),
    path('subtree/<int:id>/', v_cur.subtree, name='subtree'),
    path('tree_nav/<int:id>/', views.tree_nav, name='tree_nav'),
    path('change_txt/<int:id>/', v_cur.change_txt, name='change_txt'),
    path('change_figure/<int:id>/', v_cur.change_figure, name='change_figure'),

    path('', views.index, name='index'),
]
