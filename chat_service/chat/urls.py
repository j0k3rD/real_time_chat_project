from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.index, name='index'),
    path('group/<int:group_id>/', views.group_chat, name='group_chat'), 
    path('menu', views.chat_main_page, name='chat_main_page'),
    # path('send_message/', views.send_message, name='send_message'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)