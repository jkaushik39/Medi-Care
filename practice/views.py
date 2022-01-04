from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm


def home(request):
	return render(request,'practice/dashboard.html')

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'practice/register.html', context )

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				auth_login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'practice/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



def about(request):
    return render(request,'practice/about.html')

def contact(request):
    return render(request,'practice/contact.html')

@login_required(login_url='login')
def doc1(request):
    return render(request,'practice/doc1.html')  

@login_required(login_url='login')
def doc2(request):
    return render(request,'practice/doc2.html')

@login_required(login_url='login')
def doc3(request):
    return render(request,'practice/doc3.html')  

@login_required(login_url='login')
def doc4(request):
    return render(request,'practice/doc4.html')   

def payment(request):
    return render(request,'practice/payment.html')   

def login(request):
    return render(request,'practice/login.html') 

def register(request):
    return render(request,'practice/register.html') 

        
