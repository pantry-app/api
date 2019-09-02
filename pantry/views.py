from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import IngredientFilter, RecipeFilter
from .models import Recipe
from .serializers import (
    IngredientSerializer,
    RecipeSerializer,
    RecipeIngredientSerializer,
)


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = IngredientFilter

    def get_queryset(self):
        # Limit ingredients to user's own ingredients
        return self.request.user.ingredients.all()


class RecipeViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecipeFilter

    def get_queryset(self):
        # Limit recipes to user's own recipes
        return self.request.user.recipes.all()

    def get_serializer_class(self):
        if self.action in {"add_ingredient", "remove_ingredient"}:
            return RecipeIngredientSerializer

        return RecipeSerializer

    @action(methods=["POST"], detail=True)
    def add_ingredient(self, request, pk):
        recipe: Recipe = self.get_object()

        serializer = self.get_serializer_class()(data=request.data)

        serializer.is_valid(raise_exception=True)

        ingredient = serializer.validated_data["ingredient"]

        recipe.ingredients.add(ingredient)

        return Response(RecipeSerializer(instance=recipe).data)

    @action(methods=["POST"], detail=True)
    def remove_ingredient(self, request, pk):
        recipe: Recipe = self.get_object()

        serializer = self.get_serializer_class()(data=request.data)

        serializer.is_valid(raise_exception=True)

        ingredient = serializer.validated_data["ingredient"]

        recipe.ingredients.remove(ingredient)

        return Response(RecipeSerializer(instance=recipe).data)
