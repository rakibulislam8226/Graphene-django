import graphene
from graphene_django import DjangoObjectType
from graphene import relay, ObjectType
from .models import Category, Ingredient, CheckNewModels, TestAllFields
from django.contrib.auth.models import User
from django.db.models import Count


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
        # filter_fields = ('name', 'title', 'kind', 'category')
        convert_choices_to_enum = False
        # convert_choices_to_enum = ["kind"]
        # interfaces = (relay.Node,)


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class AllUserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id',)

    active = graphene.Int()

    def resolve_active(self, info):
        total = User.objects.all()
        length = len(total)
        return (length)


class AllEmailUserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id',)

    active = graphene.Int()

    def resolve_active(self, info):
        total = User.objects.all().values('email').annotate(total=Count('email'))
        length = len(total)
        return (length-1)


class TestAllFieldsType(DjangoObjectType):
    class Meta:
        model = TestAllFields
        fields = "__all__"
        convert_choices_to_enum = False

