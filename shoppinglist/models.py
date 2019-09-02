from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField
from uuid import uuid4


class ShoppingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = AutoCreatedField()
    modified = AutoLastModifiedField()

    complete = models.BooleanField()

    initial_ingredients = models.ManyToManyField(
        "pantry.Ingredient", related_name="shopping_lists_initial"
    )
    submitted_ingredients = models.ManyToManyField(
        "pantry.Ingredient", related_name="shopping_lists_submitted"
    )

    owner = models.ForeignKey(
        "account.User", on_delete=models.CASCADE, related_name="shopping_lists"
    )
