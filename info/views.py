from django.shortcuts import render
from .models import LikeModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def Info(request):
    return render(request, 'info/info.html')

@login_required
def InfoLike(request):
    Info = get_object_or_404(Info, slug=slug)
    if Info.likes.filter(id=request.user.id).exists():
         Info.likes.remove(request.user)
    else:
        post.likes.add(request.user)

return HttpResponseRedirect(reverse('Info', args=[str(pk)]))


def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data        