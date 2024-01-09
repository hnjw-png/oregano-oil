from django.shortcuts import render
from .models import LikeInfo

# Create your views here.
def Info(request):
    return render(request, 'info/info.html')


def like(request):
    Info = get_object_or_404(Info, slug=slug)
    if Info.likes.filter(id=request.user.id).exists():
         Info.likes.remove(request.user)
    else:
        post.likes.add(request.user)