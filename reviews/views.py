from rest_framework import generics
from django.http import JsonResponse
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class ReviewListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse(
                {"detail": "❌ Review deleted successfully!"}, status=204
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
