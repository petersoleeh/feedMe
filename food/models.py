from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    food_pic = models.ImageField(upload_to = 'food/',blank = True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    rest_img = models.ImageField(upload_to = 'restaurant/',blank = True)
    name = models.CharField(max_length=200)
    rest_desc = models.CharField(max_length=200)
    menu = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    website_url = models.CharField(max_length=500,blank=True)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    price = MoneyField(decimal_places=2,default=0,default_currency='USD',max_digits=11)

    def __str__(self):
        return self.name
