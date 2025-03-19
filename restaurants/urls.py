from rest_framework.routers import DefaultRouter

from .views import RestaurantView,MenuView
from django.urls import path

router=DefaultRouter()
router.register("", RestaurantView)

urlpatterns=[
    path("<int:restaurant_id>/menu/", MenuView.as_view({'get':'list', 'post':'create'}), name='restaurant-menus'),
    path("<int:restaurant_id>/menu/<int:pk>/", MenuView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}), name='restaurant-menu-details')
]

urlpatterns += router.urls

