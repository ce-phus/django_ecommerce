from .views import index, register, account_details, update_account, delete_account, address_list, address_detail, create_address, update_address, delete_address, order_list, change_order_status
from django.contrib.auth import views as auth_views
from django.urls import path 

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name= 'login'),
    path('account/', account_details, name= 'account_details'),
    path('account/update-account/', update_account, name= 'update_account'),
    path('account/delete-account/', delete_account, name= 'delete_account'),
    path('address-list/', address_list, name='address_list'),
    path('address/create-address/', create_address, name='create_address'),
    path('address/update-address/', update_address, name='update_address'),
    path('address/delete-address', delete_address, name='delete_address'),
    path('order/', order_list, name='order_list'),
    path('order/change-order', change_order_status, name='change_order_status'),
]
