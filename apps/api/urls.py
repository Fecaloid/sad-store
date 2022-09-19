from django.urls import path, include
from apps.user import views


urlpatterns = [
    path('user/', include('apps.api.user.urls'))
]
