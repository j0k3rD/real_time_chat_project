from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('token/', views.get_token_page, name='get_token'),
    path('menu/', views.get_main_page, name='main_page'),
    path('group/<int:group_id>/', views.get_group, name='group_chat'), 
    path('health_check/', views.health_check), 
    path('group_chat/<int:group_id>/', views.get_group_chat, name='group_chat'),
    path('logout/', views.logout, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)