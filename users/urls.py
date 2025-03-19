from rest_framework.routers import DefaultRouter

from .views import UserViewSet,LoginView
from django.urls import path

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns=[
    path('login/', LoginView.as_view())
]

urlpatterns += router.urls
