from rest_framework.routers import DefaultRouter

from .views import CartViewSet, OrderViewSet,OrderItemViewSet
from django.urls import path

router=DefaultRouter()
router.register('orders', OrderViewSet, basename='orders-user')
router.register('orders-item', OrderItemViewSet, basename='orders-user-items')

urlpatterns=[
    path('users/<int:user_id>', CartViewSet.as_view({'get':'list'}), name='user-cart')
]

urlpatterns += router.urls
