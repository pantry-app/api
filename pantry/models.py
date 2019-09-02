from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from uuid import uuid4

from .choices import INGREDIENT_STATUS_CHOICES


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = AutoCreatedField()
    modified = AutoLastModifiedField()

    name = models.CharField(max_length=128)
    active = models.BooleanField()
    url = models.URLField()
    notes = models.TextField()

    owner = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="recipes"
    )

    def __str__(self):
        return f"<Recipe - {self.name}>"


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = AutoCreatedField()
    modified = AutoLastModifiedField()

    name = models.CharField(max_length=128)
    active = models.BooleanField()
    notes = models.TextField()
    status = models.CharField(max_length=16, choices=INGREDIENT_STATUS_CHOICES)

    owner = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="ingredients"
    )
    recipes = models.ManyToManyField(Recipe, related_name="ingredients")

    def __str__(self):
        return f"<Ingredient - {self.name}>"
