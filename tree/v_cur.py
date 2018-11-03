from django.shortcuts import render, get_object_or_404
from .models import MagicNode
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

def msg(request,msg):
    return render(request, 'msg.html', {'msg': msg})

class AddItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    location = forms.IntegerField(widget=forms.HiddenInput())

class UnameForm(forms.Form):
    uname = forms.SlugField(required = False)

def add_item(request,id,location):
    old_node = MagicNode.objects.get(id=id)
    owner = request.user
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddItemForm(request.POST)
        form2 = UnameForm(request.POST)
        if form2.is_valid():
            uname = form2.cleaned_data['uname']
            if uname == '':
                uname = 'jacobfeldman'
            owner = User.objects.get(username = uname)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            location = int(form.cleaned_data['location'])

            new_node = MagicNode(desc=name,owner=owner)
            if location == 1:
                old_node.add_sibling('left',instance=new_node)
            elif location == 2:
                old_node.add_sibling('right',instance=new_node)
            else:
                old_node.add_child(instance=new_node)

            return msg(request,'child created')
        else:
            return msg(request,'cannnot create child')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddItemForm(initial={'location':location})
        form2 = UnameForm()

        return render(request, 'add_item.html',
            {'form': form,
            'form2':form2,
            'old_node':old_node,
            'location':location,
            })

def subtree(request,id):
    node = MagicNode.get_first_root_node()
    if id!=0:
        node = MagicNode.objects.get(id=id)
    annotated_list = MagicNode.get_annotated_list(parent=node)
    return render(request,'tree.html',
                    {'annotated_list':annotated_list,
                     })

def tree(id):
    children = []
    siblings = []
    parent = None
    node = None
    get = lambda node_id: MagicNode.objects.get(pk=node_id)
    try:
        try:
            node = get(id)
        except:
            node = MagicNode.get_first_root_node()

        if node.is_root():
            node = node.get_first_child()

        try:
            parent = node.get_parent()
            children = node.get_children()
            siblings = node.get_siblings()
        except:
            pass

    except:
        pass
    return   {
            'node':node,
             'children':children,
             'parent':parent,
             'siblings':siblings,
             }

class ChangeTxtForm(ModelForm):
    class Meta:
        model = MagicNode
        fields = [
        'desc', 'text', 'sites',
        'sib_order', 'video',
        'is_ready','has_exam']

def change_txt(request,id):
    node = get_object_or_404(MagicNode, id=id)
    form = ChangeTxtForm(request.POST or None, instance=node)
    if form.is_valid():
        node = form.save()
        return msg(request,'change request done')

    return render(request, 'change_txt.html',
                {'form': form, 'node':node
                })

class ChangeFigureForm(ModelForm):
    class Meta:
        model = MagicNode
        fields = ['figure']

def change_figure(request,id):
    node = MagicNode.objects.get(id=id)
    form = ChangeFigureForm(request.POST or None, request.FILES or None, instance = node)
    if form.is_valid():
        node = form.save()
        return msg(request,'change request done')

    return render(request, 'change_figure.html',
            {'form': form, 'node':node
            })
