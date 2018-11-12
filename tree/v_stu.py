from django import forms
from django.forms import ModelForm

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Profile, MagicNode, Ticket
from .v_cur import tree, msg

def kid2book(request,id):
    kid = User.objects.get(id=id)
    qs = Ticket.objects.filter(student=kid).order_by('-created_at')
    return render(request,'kid2book.html',
        {
        'kid':kid,
        'qs':qs,
        }
    )
