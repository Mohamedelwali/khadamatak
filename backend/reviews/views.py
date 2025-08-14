from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from services.models import Service
from .serializers import ReviewSerializer

# -------- Reviews for a Service --------
@api_view(["GET", "POST"])
def service_reviews(request, service_id):
    """
    GET: list reviews for a specific service
    POST: create a review for that service
    """
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
            return Response({"message": "Review created", "review": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------- Single Review CRUD --------
@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, pk):
    """
    GET: retrieve a review by ID
    PUT: update a review by ID
    DELETE: delete a review by ID
    """
    review = get_object_or_404(Review, pk=pk)

    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Review updated", "review": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        review.delete()
        return Response({"message": "Review deleted"}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)