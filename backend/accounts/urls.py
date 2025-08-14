from django.urls import path
from .views import ProfilesListView, ProfileUpdateView, MyProfileView, MeView, ChangePasswordView, RegisterView

urlpatterns = [
      path('register/', RegisterView.as_view(), name='register'),
    path('profiles/', ProfilesListView.as_view(), name='profiles-list'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/me/', MyProfileView.as_view(), name='my-profile'),
    path('me/', MeView.as_view(), name='me'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'), 
]