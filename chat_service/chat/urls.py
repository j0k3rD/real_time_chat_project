from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('group/<int:group_id>/', views.group_chat, name='group_chat'), 
    path('menu/', views.chat_main_page, name='chat_main_page'),
    path('health_check/', views.health_check),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)