from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import login

def index(request):
    if not request.session.get('exists',False):
        return render(request,"login.html")
    else:
        return redirect('/dashboard')

@csrf_exempt
def doLogin(request):
    if not request.session.get('exists',False):
        return login.doLogin(request)
    else:
        return redirect('/dashboard')

def loginError(request):
    return render(request,"loginError.html")

def dashboard(request):
    return HttpResponse('Teste')
