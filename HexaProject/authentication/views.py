from doctest import FAIL_FAST
from pickle import TRUE
from django.shortcuts import render, redirect

from .models import User
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.
def owner_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        
        if form.is_valid():
            form.save()
            uobj = User.objects.get(username=username)           
            uobj.save()
            return redirect('/auth/OwnerLogin/')
    context = {'form': form }
    return render(request, 'OwnerRegistration.html', context)



def owner_login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_data_owner) == 1:
                login(request, user)
                return redirect('/owner/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'OwnerLogin.html', context)





def home(request):
    return render(request , 'LoginPage.html')


def regulator_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        
        if form.is_valid():
            form.save()
            uobj = User.objects.get(username=username)           
            uobj.save()
            return redirect('/auth/RegulatorLogin/')
    context = {'form': form }
    return render(request, 'Regulator/RegulatorRegistration.html',context)



def regulator_login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_regulators) == 1:
                login(request, user)
                return redirect('/regulator/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'Regulator/RegulatorLogin.html',context)

def analyst_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        
        if form.is_valid():
            form.save()
            uobj = User.objects.get(username=username) 
            uobj.is_analyst=1  
            uobj.is_regulators=0 
            uobj.is_data_owner=0                 
            uobj.save()
            return redirect('/auth/AnalystLogin/')
    context = {'form': form }
    return render(request, 'Analyst/AnalystRegistration.html',context)



def analyst_login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_analyst) == 1:
                login(request, user)
                return redirect('/analyst/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'Analyst/AnalystLogin.html',context)
