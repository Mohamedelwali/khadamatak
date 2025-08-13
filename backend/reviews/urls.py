from django.urls import path
from . import views

urlpatterns = [
    path("service/<int:service_id>/", views.service_reviews, name="service_reviews"),
    path("<int:pk>/", views.review_delete, name="review_delete"),
]
