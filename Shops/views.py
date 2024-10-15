from rest_framework.views import APIView
from rest_framework import status
from .models import Shop
from .serializers import ShopSerializer
import math
from django.http import JsonResponse

class Shops(APIView):
    def get(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return JsonResponse({
            'success':True,
            'data':serializer.data
            },status = status.HTTP_200_OK)

class CreateShop(APIView):
    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'success':True,
                'message':'Shop registered successfully',
                'data':serializer.data
                }, status=status.HTTP_201_CREATED)
        return JsonResponse({
            'success':False,
            'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

class SearchShops(APIView):
    def post(self, request):
        user_lat = float(request.data.get('latitude'))
        user_lon = float(request.data.get('longitude'))

        shops = Shop.objects.all()
        shop_distances = []

        for shop in shops:
            distance = haversine(user_lat, user_lon, float(shop.latitude), float(shop.longitude))
            shop_distances.append((shop, distance))

        shop_distances.sort(key=lambda x: x[1])  # Sort by distance
        sorted_shops = [shop for shop, distance in shop_distances]

        serializer = ShopSerializer(sorted_shops, many=True)
        serialized_data = serializer.data

        for i, shop_data in enumerate(serialized_data):
            shop_data['distance'] = str(round(shop_distances[i][1],2))+" KM"


        return JsonResponse({
            'success':True,
            'data':serialized_data
            },status=status.HTTP_200_OK)