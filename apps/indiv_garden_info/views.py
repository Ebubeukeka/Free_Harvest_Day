from django.shortcuts import render, redirect
# from django.contrib import messages
from .models import Garden

def click_test(request):
    return render(request,'indiv_garden_info/click_test.html')

def gardens(request):
    return render(request,"indiv_garden_info/gardens.html")

def garden_registration(request):
    Garden.objects.create(garden_name=request.POST['garden_name'],garden_address=request.POST['garden_address'],plant_date=request.POST['plant_date'],plans=request.POST['plans'])
    garden=Garden.objects.last()
    garden_id=garden.id
    return redirect("/gardens")

def garden_request(request):
    return render(request, "indiv_garden_info/garden_request.html")

# def map(request):
#     location = request.POST['l']
# Create your views here.
