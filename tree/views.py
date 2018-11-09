from django import forms

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .v_cur import tree

def index(request):
    return render(request,'index.html')

def tree_nav(request,id=1):
    d = tree(id)
    return render(request,'tree_nav.html',d)

class Kid2ParentForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['parent','user']

    def __init__(self, *args, **kwargs):
       master = kwargs.pop('master')
       super(Kid2ParentForm, self).__init__(*args, **kwargs)
       self.fields["user"].queryset = User.objects.filter(
                profile__master=master,profile__role='S')
       self.fields["parent"].queryset = User.objects.filter(
                profile__master=master,profile__role='P')

def kid2parent(request):
    form = Kid2ParentForm(request.POST or None, master=request.user)
    if form.is_valid():
        form.save()
    return render(request,'form.html', {'form':form})

class ParentKidRootForm(forms.Form):
    kid = forms.ChoiceField()
    root = forms.IntegerField()

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(ParentKidRootForm, self).__init__(*args, **kwargs)
       self.fields["kid"].queryset = User.objects.filter(profile__parent=user)
       print(self.fields["kid"].queryset)
       self.fields["root"].default = 1

def i_par(request):
    form = ParentKidRootForm(user=request.user)

    return render(request,'i_par.html',{'form':form})

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

def i_adm(request):
    return render(request,'i_adm.html')

TUT_ROLES = [
    ('P','Родитель'),
    ('S','Ученик'),
]

DIR_ROLES = [
    ('T','Тьютор'),
    ('Z','Учитель'),
    ('W','Автор учебника'),
]

ADM_ROLES = DIR_ROLES + TUT_ROLES + [('D','Директор')]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','master','parent']
    def __init__(self, *args, **kwargs):
       type = kwargs.pop('type')
       super(ProfileForm, self).__init__(*args, **kwargs)
       if type == 'A':
           ch = ADM_ROLES
       elif type == 'D':
           ch = DIR_ROLES
       else:
           ch = TUT_ROLES

       self.fields["role"].choices = ch

from django.contrib import messages

def register(request,type):
    f_user = UserCreationForm(request.POST or None)
    f_role = ProfileForm(request.POST or None, type=type)
    if request.method == 'POST':
        if f_user.is_valid() and f_role.is_valid():
            user = f_user.save()
            profile = f_role.save(commit=False)
            profile.user = user
            profile.master = request.user
            profile.save()
            return index(request)
        else:
            print('bad')
            messages.error(request, "Error")

    return render(request, 'signup2.html',{'form': f_user,'form2': f_role,
                            })

def register_adm(request):
    return register(request,'A')


def register_dir(request):
    return register(request,'D')

def register_tut(request):
    return register(request, 'T')
