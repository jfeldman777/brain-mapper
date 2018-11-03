from django.shortcuts import render, get_object_or_404
from .models import MagicNode
from django.forms import ModelForm

def msg(request,msg):
    return render(request, 'msg.html', {'msg': msg})

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
