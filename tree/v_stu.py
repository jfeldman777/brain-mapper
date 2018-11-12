from django import forms
from django.forms import ModelForm

from django.forms.widgets import NumberInput

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Profile, MagicNode, Ticket
from .v_cur import tree, msg
from .views import i_tut

def kid2book(request,id):
    kid = User.objects.get(id=id)
    qs = Ticket.objects.filter(student=kid).order_by('-created_at')
    return render(request,'kid2book.html',
        {
        'kid':kid,
        'qs':qs,
        }
    )

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['book','teacher']
        widgets = {'book':NumberInput}
        labels = {'book':'book_id'}

    def __init__(self, *args, **kwargs):
       master = kwargs.pop('master')
       super(TicketForm, self).__init__(*args, **kwargs)
       self.fields['teacher'] = forms.ModelChoiceField(
            queryset=User.objects.filter(
                     profile__master=master,profile__role='Z'))


def book_add(request,id):
    user = request.user
    student = User.objects.get(id=id)
    form = TicketForm(request.POST or None, master=user)
    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.student = student
        ticket.save()
        return msg(request,'done')
    return render(request,'form.html',{'form':form})

def book_edit(request,id):
    user = request.user
    ticket = Ticket.objects.get(id=id)
    form = TicketForm(request.POST or None, instance=ticket, master=user)
    if form.is_valid():
        form.save()
        return msg(request,'done')
    return render(request,'form.html',{'form':form})

def book_del(request,id):
    ticket = Ticket.objects.get(id=id)
    ticket.delete()
    return i_tut(request)
