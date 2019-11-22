from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="admin/")
def index(request):
    return render(request,'index.html')



# kfshdkfskufhsughsig
@login_required(login_url="/")
def reports(request):
    return render(request,'reports.html')

@login_required(login_url="/")
def tables(request):
    return render(request,'tables.html')

    

def logout(request):
    auth.logout(request)
    return ('/')

