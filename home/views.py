from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactMailForm

def contactView(request):
    if request.method == "GET":
        form = ContactMailForm()
    else:
        form = ContactMailForm(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data["name"]
                email = form.cleaned_data["email"]
                message = form.cleaned_data['message']
                form.save()
                # needs crednetials before it will work
                #send_mail(name, message, email, ["admin@buildly.io"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "home/contact.html", {"form": form})

def successView(request):
    return render(request, "home/success.html")
