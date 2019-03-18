from django.urls import path
from . import views


urlpatterns = [
    path('', views.show, name='show'),
    path('search/', views.search, name='search'),
    path('login/', views.do_login, name='do_login'),
    path('operate/', views.do_operate, name='do_operate'),
    path('postmanage/', views.do_post, name='do_post'),
    path('card/', views.card_record, name="card_record"),
]
