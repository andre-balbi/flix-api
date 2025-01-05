from rest_framework import generics
from rest_framework.permissions import isAuthenticated
from django.http import JsonResponse
from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (isAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse(
                {"detail": "🎉 Actor deleted successfully!"}, status=204
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
