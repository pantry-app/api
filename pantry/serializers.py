from rest_framework import serializers

from .choices import INGREDIENT_STATUS_CHOICES
from .models import Ingredient, Recipe


class IngredientSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    name = serializers.CharField(required=True)
    active = serializers.BooleanField(required=False, default=True)
    notes = serializers.CharField(required=False, allow_blank=True)
    status = serializers.ChoiceField(
        choices=INGREDIENT_STATUS_CHOICES,
        required=False,
        default=INGREDIENT_STATUS_CHOICES.empty,
    )

    class Meta:
        model = Ingredient
        fields = ("id", "name", "active", "notes", "status", "owner")


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    ingredients = IngredientSerializer(many=True, required=False)

    name = serializers.CharField(required=True)
    active = serializers.BooleanField(required=False, default=True)
    notes = serializers.CharField(required=False, allow_blank=True)
    url = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Recipe
        fields = ("id", "name", "active", "notes", "url", "ingredients", "owner")


class RecipeIngredientSerializer(serializers.Serializer):
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
