from django.urls import path
from .views import Shops, CreateShop, SearchShops

urlpatterns = [
    path('shops/', Shops.as_view(), name='shop_list'),
    path('shops/register/', CreateShop.as_view(), name='shop_create'),
    path('shops/search/', SearchShops.as_view(), name='search_shop'),
]
