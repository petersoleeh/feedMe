from django.shortcuts import render
from .models import Food
# Create your views here.
def index(request):
    food = Food.objects.all()
    return render(request,'index.html',{"food":food})
