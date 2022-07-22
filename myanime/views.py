from email import message
from imaplib import _Authenticator
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def home(request):
    context = {}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = _Authenticator(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'Invalid username or password')
        return redirect('login/')
    return render(request, 'blog/login.html')


def logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(
            firstname, lastname, username, email, password)
        user.save()
    # else:
        # return redirect('login/')

    return render(request, 'blog/register.html')
