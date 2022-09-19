from django.urls import path, include

from apps.api.user.views import LoginView
from apps.user import views


urlpatterns = [
    path('login/', LoginView.as_view(), name='api_login')
]
