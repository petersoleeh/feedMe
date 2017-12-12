from django.contrib import admin
from .models import Food,Restaurant

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields': ['name','rest_desc','menu']}),
                 ('Contact',{'fields':['website_url','phone_number']}),
                 ('Food',{'fields':['food']}),
                 ('Pictures',{'fields':['rest_img']}),]

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food)
