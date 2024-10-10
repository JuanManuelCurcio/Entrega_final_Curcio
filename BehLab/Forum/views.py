from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import * 
from .forms import *

def forum_view(req):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(req,'forum_view.html',context)
 
def addInForum(req):
    form = CreateInForum()
    if req.method == 'POST':
        form = CreateInForum(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(req,'addInForum.html',context)
 
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)