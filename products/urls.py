from django.urls import path 
from . import views
from .views import TFTsView, TFTsDetailView, TFTsDeleteView, TFTsCreateView, TFTsEditView

urlpatterns = [
    path('', TFTsView.as_view(), name = 'tft_list'),
    path('tft/<str:pk>/', TFTsDetailView.as_view(), name='tft_details'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update-cart-quantity/<int:item_id>/<int:quantity>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('cart/', views.cart_detail, name='cart_detail'),
     path('api/cart-summary/', views.cart_summary, name='cart_summary'),
]