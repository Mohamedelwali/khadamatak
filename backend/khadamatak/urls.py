from django.contrib import admin
from django.urls import path, include
from bookings.views import booking_list, booking_detail
from rest_framework.routers import DefaultRouter
from invoices.views import InvoiceViewSet  

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', booking_list, name='booking-list'),
    path('bookings/<int:pk>/', booking_detail, name='booking-detail'),
<<<<<<< HEAD
    path('', include(router.urls)),  
=======

    # Services app endpoints
    path('api/services/', include('services.urls')),

    # Reviews app endpoints
    path('api/reviews/', include('reviews.urls')),

>>>>>>> master
]
