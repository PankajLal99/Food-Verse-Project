from django.urls import path
from . import views

urlpatterns = [
    path('get-all-area-markets/', views.get_all_area_market_list, name='all_area_market_list'),
]