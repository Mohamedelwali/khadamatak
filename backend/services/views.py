from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Service, ServiceCategory
from .serializers import ServiceSerializer, ServiceDetailSerializer, ServiceCategorySerializer
from .utils import filter_services

# -------- Categories --------
@api_view(["GET", "POST"])
def service_categories(request):
    if request.method == "GET":
        categories = ServiceCategory.objects.all()
        serializer = ServiceCategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ServiceCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def service_category_detail(request, pk):
    category = get_object_or_404(ServiceCategory, pk=pk)

    if request.method == "GET":
        serializer = ServiceCategorySerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ServiceCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response({"message": "Category deleted"}, status=status.HTTP_200_OK)

# -------- Services --------
@api_view(["GET", "POST"])
def service_list(request):
    if request.method == "GET":
        services = Service.objects.annotate(
            rating_avg=Avg("reviews__rating"),
            rating_count=Count("reviews")
        )
        services = filter_services(services, request.query_params)
        serializer = ServiceDetailSerializer(services, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def service_detail(request, pk):
    service = get_object_or_404(
        Service.objects.annotate(
            rating_avg=Avg("reviews__rating"),
            rating_count=Count("reviews")
        ),
        pk=pk
    )

    if request.method == "GET":
        serializer = ServiceDetailSerializer(service)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        service.delete()
        return Response({"message": "Service deleted"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
