from . import models
from .types import CategoryType, IngredientType

def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return models.Ingredient.objects.select_related("category").all()

def resolve_category_by_name(root, info, name):
    try:
        return models.Category.objects.get(name=name)
    except models.Category.DoesNotExist:
        return None