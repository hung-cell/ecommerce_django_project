from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.productDetail, name='product'),
    path('search/', views.searchBar, name='search'),
    path('update_cart/', views.updateCart, name='update_cart'),

]
