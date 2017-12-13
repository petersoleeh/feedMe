from django.shortcuts import render
from .models import Food,Restaurant
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    food = Food.objects.all()
    return render(request,'index.html',{"food":food})


def restaurant(request,food_id):
    rest = Restaurant.objects.filter(food_id=food_id)
    try:
        food = Food.objects.get(pk=food_id)

    except Food.DoesNotExist:
        raise Http404("This Item isn't available")


    print(rest)
    return render(request,'all-food/restaurant.html',{"rest":rest})


@login_required(login_url='/accounts/register/')
def restaurant_details(request,restaurant_id):
    try:
        rest = Restaurant.objects.get(pk=restaurant_id)
    except Restaurant.DoesNotExist:
        raise Http404("That Restaurant Does Not Exist")

    restaurants = Restaurant.objects.filter(id=restaurant_id)

    return render(request,'all-food/restaurant-details.html',{"restaurants":restaurants})
