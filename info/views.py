from django.shortcuts import render
from .models import LikeModel
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def Info(request):
    return render(request, 'info/info.html')

@login_required
def AddLike(request, *args, **kwargs):
    instance = LikeModel.objects.all().first()
    
    if instance == None:
        instance = LikeModel.objects.create()
        instance.save()
        
    if instance.likes.all().filter(id=request.user.id).exists():
        instance.dislikes.remove(request.user.id)
    else:
        instance.likes.add(request.user.id)
        
    return render(request, 'info/info.html')

            
@login_required
def AddDislike(request, *args, **kwargs):
    instance = LikeModel.objects.all().first()
    
    if instance == None:
        instance = LikeModel.objects.create()
        instance.save()
        
    if instance.dislikes.all().filter(id=request.user.id).exists():
        instance.likes.remove(request.user.id)
    else:
        instance.dislikes.add(request.user.id)
        
    return render(request, 'info/info.html')

