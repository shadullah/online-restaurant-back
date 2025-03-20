from django.shortcuts import render,get_object_or_404
from .serializers import CartSerializer,OrderSerializer, OrderItemSerializer
from .models import Cart,Order,OrderItem

from rest_framework import viewsets

# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        user_id=self.kwargs.get('user_id')
        if user_id:
            return Cart.objects.filter(user_id=user_id)
        return Cart.objects.all()
    
    def perform_create(self, serializer):
        user_id=self.kwargs.get('user_id')
        serializer.save(user_id=user_id)
    
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id=self.kwargs.get('user_id')
        if user_id:
            return Order.objects.filter(user_id=user_id)
        return Order.objects.all()
    
class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        user_id=self.kwargs.get('user_id')
        if user_id:
            return Order.objects.filter(user_id=user_id)
        return OrderItem.objects.all()