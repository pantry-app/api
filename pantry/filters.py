from django_filters import rest_framework as filters

from .models import Recipe, Ingredient


class RecipeFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Recipe
        fields = ("name",)


class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Ingredient
        fields = ("name",)
