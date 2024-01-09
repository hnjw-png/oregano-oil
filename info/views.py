from django.shortcuts import render

# Create your views here.
def Info(request):
    return render(request, 'info/info.html')