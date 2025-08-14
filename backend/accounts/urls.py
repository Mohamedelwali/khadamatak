from django.urls import path , include
from .views import ProfilesListView, ProfileUpdateView, MyProfileView, MeView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    # Djoser base endpoints (register, activate, reset password, etc.)
    path('', include('djoser.urls')),

    # Profile endpoints
    path('profiles/', ProfilesListView.as_view(), name='profiles-list'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/me/', MyProfileView.as_view(), name='my-profile'),
    path('me/', MeView.as_view(), name='me'),
]