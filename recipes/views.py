from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)