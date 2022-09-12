from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=100)
    numbering = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="dishes")
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    img = models.ImageField(upload_to='article')
    price = models.IntegerField()
    gram = models.IntegerField()

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=10, unique=True)
    symbol = models.CharField(max_length=3)
