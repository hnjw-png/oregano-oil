from django.shortcuts import render
from .models import LikeModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def Info(request):
    return render(request, 'info/info.html')

@login_required
def LikeRequest(request):
    Info = get_object_or_404(Info, slug=slug)
    if Info.likes.filter(id=request.user.id).exists():
         Info.likes.remove(request.user)
    else:
        post.likes.add(request.user)