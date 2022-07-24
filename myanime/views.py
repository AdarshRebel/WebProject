from django.shortcuts import  render
from django.contrib.auth.decorators import login_required

from .models import *


@login_required(login_url="login")
def home(request):
    return render(request,'blog/home.html',)

@login_required(login_url="login")
def download(request):
    return render(request,'blog/download.html')

def new(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'blog/new.html',context)

