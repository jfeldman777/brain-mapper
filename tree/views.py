from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

def index(request):
    return render(request,'index.html')

def i_cur(request):
    return render(request,'i_cur.html')

def i_par(request):
    return render(request,'i_par.html')

def i_stu(request):
    return render(request,'i_stu.html')

def i_tea(request):
    return render(request,'i_tea.html')

def i_gue(request):
    return render(request,'i_gue.html')

def i_tut(request):
    return render(request,'i_tut.html')

def i_dir(request):
    return render(request,'i_dir.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
