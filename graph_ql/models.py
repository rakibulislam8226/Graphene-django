from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="ingredients", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class CheckNewModels(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    category = models.ForeignKey(
        Category, related_name="cat", on_delete=models.CASCADE
    )
    kind = models.CharField(max_length=100, choices=(("cat", "Cat"), ("dog", "Dog")))

    def __str__(self):
        return self.name