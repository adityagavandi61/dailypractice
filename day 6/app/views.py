from django.shortcuts import render
from app.forms import RegistrationForm,LoginForm
# Create your views here.

def forms_as_p(request):
    form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request,'registration.html',context)

def forms_for(request):
    form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request,'regisinput.html',context)

def login(request):
    form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'login.html',context)