from django.urls import path

from apps.main.views import PageView, home

urlpatterns = [
    path('', home, name='home'),
    path('<str:slug>/', PageView.as_view(), name='page'),
]
