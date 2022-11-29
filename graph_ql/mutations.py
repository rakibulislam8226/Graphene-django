import graphene
from . import models
from . import types
from . import serializer
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation


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
        print("thank")
        category.delete()
