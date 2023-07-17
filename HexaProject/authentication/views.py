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
            return redirect('owner')
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

def coordinatorlogin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_coordinator) == 1:
                login(request, user)
                return redirect('/coordinator/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'ProgramCoordinatorLoginPage.html', context)

def instructorlogin(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password = password)
            if (user is not None) and (user.is_instructor == 1):
                login(request, user)
                return redirect('/instructor/')
            else:
                messages.info(request, "Username or Password is incorrect.")
        context = {}
        return render(request, 'ProgramInstructorLoginPage.html', context)

def home(request):
    return render(request , 'LoginPage.html')