from rest_framework.routers import DefaultRouter

from .views import UserViewSet,LoginView
from django.urls import path

# router = DefaultRouter()
# router.register('', UserViewSet)

urlpatterns=[
    path('', UserViewSet.as_view({'get':'list', 'post':'create'}), name="user-list"),
    path('/<int:pk>', UserViewSet.as_view({'get':'retrieve'}), name="userDetail"),
    path('/login', LoginView.as_view())
]

# urlpatterns += router.urls
