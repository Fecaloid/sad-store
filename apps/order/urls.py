from django.urls import path
from apps.order import views


urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('create/', views.create_order, name='create_order'),
]
