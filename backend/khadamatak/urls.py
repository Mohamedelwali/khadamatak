"""
URL configuration for khadamatak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from bookings.views import booking_list, booking_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', booking_list, name='booking-list'),
    path('bookings/<int:pk>/', booking_detail, name='booking-detail'),

    # Services app endpoints
    path('api/services/', include('services.urls')),

    # Reviews app endpoints
    path('api/reviews/', include('reviews.urls')),

=======

urlpatterns = [

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/accounts/', include('accounts.urls')),
>>>>>>> 9a867c4 (create dashboard for worker and clients)
]
