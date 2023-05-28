from . import views
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('', views.ProductsView.as_view(), name='products'),
    path('product/<slug>/', views.ProductView.as_view(), name='product'),
    path('thank/', views.thank, name='thank'),
    path('order-summary/', views.OrderSummaryView.as_view(), name='order_summary'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('add-single-to-cart/<slug>/', views.add_single_to_cart, name='add_single_to_cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove-single-from-cart/<slug>/', views.remove_single_item_from_cart, name='remove_single_from_cart'),
]