import graphene
from . import models
from . import types
from . import serializer
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation

# Check new models start #
class CreateCheckNewModelsMutation(SerializerMutation):
    class Meta:
        serializer_class = serializer.CheckNewModelsSerializer
        model_operations = ['create']
        # lookup_field = 'id'
        convert_choices_to_enum = False

    # @classmethod
    # def mutate(cls, root, info, **kwargs):
    #     if kwargs['input'].get('kind'):
    #         kwargs["input"]["kind"] = kwargs["input"]["kind"].split(",")
    #     return super().mutate(root, info, **kwargs)


class UpdateCheckNewModelsMutation(SerializerMutation):
    class Meta:
        serializer_class = serializer.CheckNewModelsSerializer
        convert_choices_to_enum = False
        model_operations = ['update']
        lookup_field = 'id'

    # @classmethod
    # def get_serializer_kwargs(cls, root, info, **input):
    #     if 'id' in input:
    #         instance = models.CheckNewModels.objects.filter(
    #             id=input['id']).first()
    #         if instance:
    #             if input.get('category') == '':
    #                 input['category'] = instance.category.id
    #             return {'instance': instance, 'data': input, 'partial': True}
    #         else:
    #             raise ValueError("Data not found")
    #
    #     return {'data': input, 'partial': True}


class DeleteCheckNewModelsMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True, description="Delete Category ID.")

    category = graphene.Field(types.CheckNewModelsType)

    @classmethod
    def mutate(cls, root, info, id):
        category = models.CheckNewModels(id=id)
        category.delete()


# Check new models End #


# Ingredients start #
class CreateIngredients(SerializerMutation):
    class Meta:
        serializer_class = serializer.IngredientSerializer
        convert_choices_to_enum = False


class UpdateIngredients(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        notes = graphene.String()
        category = graphene.ID()

    ingredients = graphene.Field(types.IngredientType)

    @classmethod
    def mutate(cls, root, info, id, **update_data):
        ingredients = models.Ingredient.objects.filter(id=id)
        if ingredients:
            params = update_data
            ingredients.update(**{k: v for k, v in params.items() if params[k]})
            return UpdateIngredients()
        else:
            print('User with given ID does not exist.')


class DeleteIngredients(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ingredients = graphene.Field(types.IngredientType)

    @classmethod
    def mutate(cls, root, info, id):
        ingredients = models.Ingredient.objects.get(id=id)
        ingredients.delete()

# Ingredients end #


# TestAllFields start #
class CreateTestAllFields(SerializerMutation):
    class Meta:
        serializer_class = serializer.TestAllFieldsSerializer
        convert_choices_to_enum = False

    @classmethod
    def mutate(cls, root, info, **kwargs):
        kwargs['input']['integradient'] = kwargs['input']['integradient'].split(',')
        return super().mutate(root, info, **kwargs)


# class UpdateTestAllFields(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID(required=True)
#         title = graphene.String()
#         integradient = graphene.ID()
#         category = graphene.ID()
#         status_selection = graphene.String()
#         max_number_events = graphene.String()
#         internal_note = graphene.String()
#         is_active = graphene.ID()
#
#     testallfield = graphene.Field(types.TestAllFieldsType)
#
#     @classmethod
#     def mutate(cls, root, info, id, **update_data):
#         testallfield = models.TestAllFields.objects.filter(id=id)
#         if testallfield:
#             params = update_data
#             testallfield.update(**{k: v for k, v in params.items() if params[k]})
#             return UpdateIngredients()
#         else:
#             print('User with given ID does not exist.')

class UpdateTestAllFields(SerializerMutation):
    class Meta:
        serializer_class = serializer.TestAllFieldsSerializer
        convert_choices_to_enum = False
        model_operations = ['update']
        lookup_field = 'id'

    @classmethod
    def mutate(cls, root, info, **kwargs):
        kwargs['input']['integradient'] = kwargs['input']['integradient'].split(',')
        return super().mutate(root, info, **kwargs)

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        if 'id' in input:
            instance = models.TestAllFields.objects.filter(
                id=input['id']).first()
            if instance:
                if input.get('category') == '':
                    input.pop('category')
                if input.get('integradient') == '':
                    input.pop('integradient')
                if input.get('internalNote') == '':
                    input.pop('internalNote')
                if input.get('statusSelection') == '':
                    input.pop('statusSelection')
                if input.get('title') == '':
                    input.pop('title')
                return {'instance': instance, 'data': input, 'partial': True}
            else:
                raise ValueError("Data not found")
        return {'data': input, 'partial': True}

class DeleteTestAllField(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    testallfield = graphene.Field(types.TestAllFieldsType)

    @classmethod
    def mutate(cls, root, info, id):
        testallfield = models.TestAllFields.objects.get(id=id)
        testallfield.delete()