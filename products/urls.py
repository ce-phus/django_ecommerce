from django.urls import path 
from . import views
from cart.views import cart_detail, success

urlpatterns = [
   path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
   path('<slug:slug>/', views.category_detail, name='category_detail'),
   path('search/', views.search, name='search'),
   path('cart/', cart_detail, name='cart'),
   path('success/', success, name='success'),
]