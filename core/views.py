from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def homePage(request):
    return render(request,'core/frontPage.html')


def signIn(request):
    
    if request.method == 'POST':

        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(request,username=uname,password=pwd)

        if user is not None:
            login(request,user)
            return redirect('shop')
        
        else:
            messages.error(request, "Cannot Login due to Invalid Credentials")
            return redirect('home')


def signUpView(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    
    form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})


def signoutView(request):
    logout(request)
    return redirect('home')


