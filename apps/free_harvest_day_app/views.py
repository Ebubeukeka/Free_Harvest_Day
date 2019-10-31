from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt

# def index(request):
#     return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def food_deserts(request):
    return render(request, 'food_deserts.html')

def register(request):
    return render(request, 'register.html')

def community(request):
    return render(request, 'community.html')
    
def events(request):
    return render(request, 'events.html')

def about(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    context = {
    "staff" : staff
    }
    return render(request, 'about_staff.html', context)


def contact_us(request):
    return render(request, 'contact_us.html')


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
            messages.error(request, 'Password incorrect')
            return render (request, 'login.html')
        else:
            request.session['user_id'] = user.id
            messages.success(request, 'Successfully Loged in')
            return redirect('/welcome')

def process_contact(request):
    errors = Contact.objects.contact_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return render(request,'contact_us.html')
    else:
        Contact.objects.create(name = request.POST['name'], contact_email = request.POST['contact_email'], message = request.POST['message'],)
        messages.success(request, 'Thank you, Information Successfully Sent!')
        return redirect('/')

def welcome(request):
    if 'user_id' not in request.session:
        # messages.error(request, '')
        context ={
            "not_logged" : True
        }
        return render (request, 'home.html', context)
    else:
        logged_user = User.objects.get(id=request.session['user_id'])
        context = {
            'user' : logged_user
        }
        return render(request, 'home.html', context)

def logout(request):
    if 'user_id' not in request.session:
        messages.error(request, 'No User Logged in, Please Sign in or Register')
        return render (request,'home.html')
    else:
        request.session.clear()
        messages.success(request, 'Successfully Logged out')
        return redirect('/')