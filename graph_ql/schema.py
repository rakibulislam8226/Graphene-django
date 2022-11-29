import graphene
from graphene import relay, ObjectType
from . import models
from . import mutations
from .types import CategoryType, IngredientType, CheckNewModelsType
from graphene_django import DjangoObjectType
from django.db.models import Q
from graphene_django import DjangoListField
from graphene_django.filter import DjangoFilterConnectionField


# from .schema import resolve_all_ingredients, resolve_category_by_name


# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi!")

# schema = graphene.Schema(query=Query)


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)  # DjangoListField = graphene.List
    category_by_id = graphene.Field(CategoryType, category_id=graphene.Int(required=True))
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    check_new_models = graphene.List(CheckNewModelsType, start_after=graphene.Int(), first=graphene.Int(),
                                     skip=graphene.Int(), search=graphene.String())
    # check_new_models_filter = DjangoFilterConnectionField(CheckNewModelsType, )

    def resolve_all_ingredients(root, info):
        return models.Ingredient.objects.select_related("category").all()

    def resolve_category_by_id(root, info, category_id):
        try:
            return models.Category.objects.get(pk=category_id)
        except models.Category.DoesNotExist:
            return None

    def resolve_category_by_name(root, info, name):
        try:
            return models.Category.objects.get(name=name)
        except models.Category.DoesNotExist:
            return None

    def resolve_check_new_models(root, info, start_after=None, first=None, skip=None, search=None):
        # print(info.context.user)

        if info.context.user.is_authenticated:
            # print(f"------ {info.context.user.is_authenticated}")
            qs = models.CheckNewModels.objects.all()
            if search:
                filter = (
                        Q(name__icontains=search) |
                        Q(title__icontains=search)
                )
                qs = qs.filter(filter)
            if start_after:
                qs = qs[start_after::]
            if skip:
                qs = qs[skip:]
            if first:
                qs = qs[:first]  # how much we want to see from first
            return qs
        else:
            return models.CheckNewModels.objects.none()

    # def resolve_check_new_models_filter(root, info):
    #     return models.CheckNewModels.objects.all()


class GraphQLMutations(graphene.ObjectType):
    create_check_new_models = mutations.CreateCheckNewModelsMutation.Field()
    update_check_new_models = mutations.UpdateCheckNewModelsMutation.Field()
    delete_check_new_models = mutations.DeleteCheckNewModelsMutation.Field()


schema = graphene.Schema(query=Query, mutation=GraphQLMutations)
