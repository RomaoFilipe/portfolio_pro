from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        # Optionally send email or notification
    return render(request, "contact.html", {"form": form})
