from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.hashers import make_password, check_password
from .models import useraccount
import pytz
import datetime

# Create your views here.
def adminapphomepage(request):
    firstname = request.session.get('firstname')
    return render(request, 'adminapp/projecthomepage.html', {'firstname': firstname})

def printer(request):
    user_input = ""
    if request.method == "POST":
        user_input = request.POST.get('klu', "")
    return render(request, 'adminapp/printer.html', {'klu': user_input})

def timetable(request):
    return render(request, 'adminapp/timetable.html')

def time1(request):
    if request.method == 'POST':
        klu = request.POST.get('klu')
        time1_zone = pytz.timezone(klu)
        print("Current Time is : ", datetime.datetime.now(time1_zone))
    return render(request, 'adminapp/time1.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = useraccount.objects.get(email=email)
            if check_password(password, user.password):
                request.session['firstname'] = user.firstname
                return redirect('adminapphomepage')
            else:
                return render(request, 'adminapp/login.html', {'error': 'Invalid Credentials'})
        except useraccount.DoesNotExist:
            return render(request, 'adminapp/login.html', {'error': 'User not found'})
    return render(request, 'adminapp/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'adminapp/signup.html', {'form': form})

def logout(request):
    request.session.flush()
    return redirect('adminapphomepage')
