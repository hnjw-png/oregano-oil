from django.shortcuts import render
from django.core.mail import send_mail

from .models import contact
from .forms import ContactForm

if form.is_valid():
    subject = form.cleaned_data["What's your question?"]
    message = form.cleaned_data["Write your message here."]
    sender = form.cleaned_data["sender"]
    cc_myself = form.cleaned_data["cc_myself"]

    recipients = ["hollyyeh12@gmail.com"]
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return messages.success(request, 'Contacted!')
# Create your views here.
