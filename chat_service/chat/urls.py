from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('group/<int:group_id>/', views.group_chat, name='group_chat'), 
    path('', views.chat_main_page, name='chat_main_page'),
    # path('send_message/', views.send_message, name='send_message'),
]