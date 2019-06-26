from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse
from . import getNavbar

def getDashBoard(request):

    navBar = getNavbar.navBar(request)
    
    context = {'navBarItens': navBar}
    return render(request,'dashboard.html',context)
