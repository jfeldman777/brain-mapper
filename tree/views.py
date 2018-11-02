from django import forms

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .models import Profile

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

class RoleDir(forms.Form):
    role = forms.ChoiceField(
        choices = (
            ('T','Тьютор'),
            ('H','Учитель'),
            ('C','Спец по содержанию')
        )
    )

class RoleTut(forms.Form):
    role = forms.ChoiceField(
        choices = (
            ('P','Родитель'),
            ('S','Ученик'),
        )
    )

class RoleAdm(forms.Form):
    role = forms.ChoiceField(
        choices = (
            ('D','Директор'),
            ('T','Тьютор'),
            ('H','Учитель'),
            ('C','Спец по содержанию')
            ('P','Родитель'),
            ('S','Ученик'),
        )
    )

def register_adm(request):
    if request.method == 'POST':
        f_user = UserCreationForm(request.POST)
        f_role = RoleAdm(request.POST)

        if f_user.is_valid() and f_role.is_valid():
            user = f_user.save()
            role = f_role.cleaned_data['role']
            print(role)
            Profile.objects.create(user=user,role=role)
            return render(request,'i_dir.html')

    else:
        f_user = UserCreationForm()
        f_role = RoleAdm()

    return render(request, 'signup2.html',{'form': f_user,'form2': f_role,
                            })


def register_dir(request):
    if request.method == 'POST':
        f_user = UserCreationForm(request.POST)
        f_role = RoleDir(request.POST)

        if f_user.is_valid() and f_role.is_valid():
            user = f_user.save()
            role = f_role.cleaned_data['role']
            print(role)
            Profile.objects.create(user=user,role=role)
            return render(request,'i_dir.html')

    else:
        f_user = UserCreationForm()
        f_role = RoleDir()

    return render(request, 'signup2.html',{'form': f_user,'form2': f_role,
                            })


def register_tut(request):
    if request.method == 'POST':
        f_user = UserCreationForm(request.POST)
        f_role = RoleTut(request.POST)

        if f_user.is_valid() and f_role.is_valid():
            user = f_user.save()
            role = f_role.cleaned_data['role']
            print(role)
            Profile.objects.create(user=user,role=role)
            return render(request,'i_dir.html')

    else:
        f_user = UserCreationForm()
        f_role = RoleTut()

    return render(request, 'signup2.html',{'form': f_user,'form2': f_role,
                            })
