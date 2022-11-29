from django.contrib import admin

# Register your models here.
from .models import Category, Ingredient, CheckNewModels

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(CheckNewModels)
