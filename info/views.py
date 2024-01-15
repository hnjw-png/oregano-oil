from django.shortcuts import render
from .models import LikeModel
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def Info(request):
    return render(request, 'info/info.html')

def AddLike(request, *args, **kwargs):
    is_dislike = False
    for dislike in Info.dislike.all():
        if dislike == request.user:
            is_dislike = True
            break
    if is_dislike:
        info.dislikes.remove(request.user)
    is_like = False
    for like in info.likes.all():
        if like == request.user:
            is_like = True
            break
    if not is_like: 
        info.likes.add(request.user)
    
    if is_like:
        info.likes.remove(request.user)
            
def AddDislike(request, *args, **kwargs):
    is_like = False
    for like in info.likes.all():
        if like == request.user:
            is_like = True
            break
    if is_like:
        Info.likes.remove(request.user)
    is_dislike = False
    for dislike in info.dislikes.all():
        if dislike == request.user:
            is_dislike = True
            break
    if not is_dislike: 
        info.dislikes.add(request.user)
    
    if is_dislike:
        info.dislikes.remove(request.user)
        

