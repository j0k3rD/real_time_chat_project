from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('group/<int:group_id>/', views.group_chat, name='group_chat'), 
    # path('send_message/', views.send_message, name='send_message'),
]