import graphene
from graphene_django import DjangoObjectType

from .models import Category, Ingredient, CheckNewModels


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

    count = graphene.Int()

    def resolve_count(self, info):
        return 2


class CheckNewModelsType(DjangoObjectType):
    class Meta:
        model = CheckNewModels
        fields = ("id", "name", "title", "kind", "category")
        # convert_choices_to_enum = False

