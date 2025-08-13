from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from services.models import Service
from .serializers import ReviewSerializer


@api_view(["GET", "POST"])
def service_reviews(request, service_id):
    """List or create reviews for a specific service."""
    service = get_object_or_404(Service, pk=service_id)

    if request.method == "GET":
        reviews = service.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data.copy()
        data["service"] = service.id
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def review_delete(request, pk):
    """Delete a review by ID."""
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
