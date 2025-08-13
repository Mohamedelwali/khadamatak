from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.service_categories, name="service_categories"),
    path("categories/<int:pk>/", views.service_category_detail, name="service_category_detail"),

    path("", views.service_list, name="service_list"),
    path("<int:pk>/", views.service_detail, name="service_detail"),
]
