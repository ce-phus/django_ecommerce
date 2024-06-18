from django.urls import path 
from . import views
from .views import TFTsView, TFTsDetailView, TFTsDeleteView, TFTsCreateView, TFTsEditView

urlpatterns = [
    path('', TFTsView.as_view(), name = 'tft_list')
]