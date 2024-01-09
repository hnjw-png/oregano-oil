from django.shortcuts import render
from django.core.mail import send_mail

from .models import Contact
from .forms import ContactForm

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    if form.is_valid():
       subject = form.cleaned_data["What's your question?"]
       message = form.cleaned_data["Write your message here."]
       sender = form.cleaned_data["sender"]

       recipients = ["hollyyeh12@gmail.com"]

       send_mail(subject, message, sender, recipients)
       return messages.success(request, 'Contacted!')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
