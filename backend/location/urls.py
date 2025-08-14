from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, CustomerViewSet, ServiceProviderViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'service-providers', ServiceProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
