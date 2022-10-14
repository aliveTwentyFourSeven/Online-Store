from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def HomePage(request):
    return render(request, 'mysite/index.html', {})
def Signup(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        passWord = request.POST.get('passWord')
        email = request.POST.get('email')
        fName = request.POST.get('firstName')
        lName = request.POST.get('lastName')
       
        

        user= User.objects.create_user(username=userName, email=email, password=passWord)
        user.last_name = lName
        user.first_name = fName
        user.save()
        # if User.objects.filter(username = username).first():
        # messages.error(request, "This username is already taken")
        # return redirect('home') 
        return redirect('login-page')

    return render(request, 'mysite/signup.html', {})
def Login(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        passWord = request.POST.get('passWord')
        user = authenticate(request, username=userName, password=passWord)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse("The account sign-in was incorrect")
    return render(request, 'mysite/login.html', {})
def Logout(request):
    logout(request)
    return redirect('login-page')
