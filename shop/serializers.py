from rest_framework import serializers

from .models import Cart, Order,OrderItem
from users.serializers import UserSerializer
from restaurants.serializers import MenuSerializer



class CartSerializer(serializers.ModelSerializer):
    cartItems= MenuSerializer(source='items',read_only=True)
    class Meta:
        model = Cart
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    cartItems = MenuSerializer(source='items',read_only=True)
    class Meta:
        model = OrderItem
        fields = "__all__"