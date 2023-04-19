from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from rest_framework.views import APIView
from django.http import HttpResponse


urlpatterns = [
    path('menu/', views.get_main_page, name='main_page'),
    path('group/<int:group_id>/', views.get_group, name='group_chat'), 
    path('health_check/', views.health_check),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)