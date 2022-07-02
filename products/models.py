from operator import mod
from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta :
        db_table = 'menus'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length= 45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name        

class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

    def __str__(self):
        return self.english_name

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table ='images'
    # def __str__(self):
    #     return Drink.objects.get(id=self.drink)

class Alergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'alergies'
    def __str__(self):
        return self.name

class Alergy_Drink(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    alergy = models.ForeignKey('Alergy', on_delete=models.CASCADE)

    class Meta:
        db_table = 'alergy_drink'
    # def __str__(self):
    #     return self.drink        

class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_oz = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'sizes'
    def __str__(self):
        return self.name

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    drink = models.ForeignKey('Drink',on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'nutritions'

    # def __str__(self):
    #     return self.drink        