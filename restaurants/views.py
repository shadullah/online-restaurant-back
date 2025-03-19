from django.shortcuts import render,get_object_or_404
from .models import Restaurant,Menu
from .serializers import RestaurantSerializer,MenuSerializer

from rest_framework import viewsets

# Create your views here.
class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MenuView(viewsets.ModelViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs.get('restaurant_id')
        if restaurant_id is not None:
            return Menu.objects.filter(restaurant_id=restaurant_id)
        return Menu.objects.all()
    
    def perform_create(self, serializer):
        restaurant_id = self.kwargs.get('restaurant_id')
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        serializer.save(restaurant=restaurant)