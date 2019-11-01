from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def process_register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request,'register.html')
    else:
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'],password = hash_pw,age_group = request.POST['age_group'],ethnicity = request.POST['ethnicity'],)
        request.session['user_id'] = user.id
        messages.success(request, 'Successfully Registered')
        return redirect('/welcome')

def process_login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request,'login.html')
    else:
        user_set = User.objects.filter(email=request.POST['login_email'])
        user = user_set[0]
        if not bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
            message.error(request, 'Password incorrect')
            return render (request, 'login.html')
        else:
            request.session['user_id'] = user.id
            messages.success(request, 'Successfully Loged in')
            return redirect('/welcome')

def welcome(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in or register')
        return redirect ('/')
    else:
        logged_user = User.objects.get(id=request.session['user_id'])
        context = {
            'user' : logged_user
        }
        return render(request, 'welcome.html', context)

def logout(request):
    request.session.clear()

    return redirect('/')

def garden_volunteer(request):
    context = {
        "gardens" : Garden.objects.all(),
        "volunteers": User.objects.all()
    }
    return render(request,"garden_volunteer.html", context)

def garden_registration(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in or register')
        return redirect ("/")
    else:
        Garden.objects.create(garden=request.POST['garden'],garden_address=request.POST['garden_address'],ward_num=request.POST['ward_num'],plant_date=request.POST['plant_date'],plans=request.POST['plans'])
        garden=Garden.objects.last()
        garden_id=garden.id
        return redirect("/garden_volunteer")

def volunteer_registration(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in or register')
        return redirect ("/")
    else:
        print('---------------------show id---------------')
        space=Garden.objects.get(id=request.POST['garden_id'])
        print(space.id)
        volunteer=User.objects.get(id=request.session['user_id'])
        print(volunteer.id)
        space.users.add(volunteer)
        return redirect('/garden_volunteer')