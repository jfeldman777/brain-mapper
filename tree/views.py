from django import forms
from django.forms import ModelForm

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, MagicNode, Ticket
from .v_cur import tree, msg

def my_txt(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    title = 'Change profile'
    f_user = UserTxtForm(request.POST or None, instance=user)
    f_profile = ProfileTxtForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        if f_user.is_valid() and f_profile.is_valid():
            f_user.save()
            f_profile.save()

            return index(request)
        else:
            print('bad')
            messages.error(request, "Error")

    return render(request, 'signup2.html',{'form': f_user,'form2': f_profile,
                            'title':title
                            })

class ProfileTxtForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_date']

class ChangeImgForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['img']

class UserTxtForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']


def prof_img(request,id):
    node = Profile.objects.get(user_id=id)
    form = ChangeImgForm(request.POST or None, request.FILES or None, instance = node)
    if form.is_valid():
        node = form.save()
        return msg(request,'change request done')

    return render(request, 'change_figure.html',
            {'form': form, 'node':node
            })


def see_us(request,type):
    qs = None
    if type == 'dir':
        qs = User.objects.filter(profile__role__in='D')
    elif type == 'tut':
        qs = User.objects.filter(profile__role__in='DT')
    elif type == 'all':
        qs = User.objects.filter(profile__role__in='DTZW')
    return render(request,'see_us.html',{'qs':qs})

class NameForm(forms.Form):
    topic = forms.CharField(max_length=100)

def topic_search(request):
    result = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            result = MagicNode.objects.filter(desc__icontains=topic)
    else:
        form = NameForm()

    return render(request, 'topic_search.html',
        {'form': form,
         'result': result,
        })

def index(request):
    return render(request,'index.html')

def tree_nav(request,id=1):
    d = tree(id)
    return render(request,'tree_nav.html',d)
class Kid2TeacherForm(forms.Form):
    teacher = forms.ChoiceField()
    kid = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
       master = kwargs.pop('master')
       super(Kid2TeacherForm, self).__init__(*args, **kwargs)
       self.fields['kid'] = forms.ModelChoiceField(
            queryset=User.objects.filter(
                     profile__master=master,profile__role='S'))
       self.fields['teacher'] = forms.ModelChoiceField(
            queryset=User.objects.filter(
                     profile__master=master,profile__role='Z'))
class Kid2ParentForm(forms.Form):
    parent = forms.ChoiceField()
    kid = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
       master = kwargs.pop('master')
       super(Kid2ParentForm, self).__init__(*args, **kwargs)
       self.fields['kid'] = forms.ModelChoiceField(
            queryset=User.objects.filter(
                     profile__master=master,profile__role='S'))
       self.fields['parent'] = forms.ModelChoiceField(
            queryset=User.objects.filter(
                     profile__master=master,profile__role='P'))

def kid2parent(request):
    form = Kid2ParentForm(request.POST or None, master=request.user)
    if form.is_valid():
        u = form.cleaned_data['kid']
        profile = Profile.objects.get(user=u)
        profile.parent = form.cleaned_data['parent']
        profile.save()
        return msg(request,'done')
    return render(request,'form.html', {'form':form})

def kid2teacher(request):
    form = Kid2TeacherForm(request.POST or None, master=request.user)
    if form.is_valid():
        u = form.cleaned_data['kid']
        profile = Profile.objects.get(user=u)
        profile.teacher = form.cleaned_data['teacher']
        profile.save()
        return msg(request,'done')
    return render(request,'form.html', {'form':form})

class ParentKidForm(forms.Form):
    kid = forms.ChoiceField()
    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(ParentKidForm, self).__init__(*args, **kwargs)
       self.fields['kid'] = forms.ModelChoiceField(
                   queryset=User.objects.filter(
                            profile__parent=user,profile__role='S'))

def i_par(request):
    form = ParentKidForm(request.POST or None, user=request.user)
    if form.is_valid():
        kid = form.cleaned_data['kid']
        qs = Ticket.objects.filter(student=kid).order_by('-updated_at')
        return render(request,'par2kid2book.html',
            {
            'kid':kid,
            'qs':qs,
            }
        )
    return render(request,'i_par.html',{'form':form})

def i_stu(request):
    kid = request.user
    qs = Ticket.objects.filter(student=kid).order_by('-updated_at')
    return render(request,'i_stu.html',{'qs':qs})

def i_tea(request):
    user = request.user
    qs = Ticket.objects.filter(teacher=user).order_by('student','book','updated_at')
    return render(request,'i_tea.html',
        {'qs':qs}
    )

def i_gue(request):
    return render(request,'i_gue.html')

def i_tut(request):
    user = request.user
    qs_par = User.objects.filter(profile__master=user, profile__role = 'P')
    qs_stu = User.objects.filter(profile__master=user, profile__role = 'S')
    qs_tea = User.objects.filter(profile__master=user, profile__role = 'Z')

    return render(request,'i_tut.html',
    {
        'qs_par':qs_par,
        'qs_stu':qs_stu,
        'qs_tea':qs_tea
    })

def i_dir(request):
    return render(request,'i_dir.html')

def i_adm(request):
    return render(request,'i_adm.html')

TUT_ROLES = [
    ('P','Родитель=Parent'),
    ('S','Ученик=Student'),
]

DIR_ROLES = [
    ('T','Тьютор=Tutor'),
    ('Z','Учитель=Teacher'),
    ('W','Автор учебника=Content Writer'),
]

ADM_ROLES = DIR_ROLES + TUT_ROLES + [('D','Директор=Principal')]

class ProfileForm1(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
    def __init__(self, *args, **kwargs):
       type = kwargs.pop('type')
       super(ProfileForm1, self).__init__(*args, **kwargs)
       if type == 'A':
           ch = ADM_ROLES
       elif type == 'D':
           ch = DIR_ROLES
       else:
           ch = TUT_ROLES

       self.fields["role"].choices = ch

from django.contrib import messages

def register(request,type):
    title = 'Create new user'
    f_user = UserCreationForm(request.POST or None)
    f_role = ProfileForm1(request.POST or None, type=type)
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
                            'title':title
                            })

def register_adm(request):
    return register(request,'A')


def register_dir(request):
    return register(request,'D')

def register_tut(request):
    return register(request, 'T')
