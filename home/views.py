from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Signature
from .forms import SignatureForm
import re

from django.shortcuts import render, redirect

#redirect to spanish if the url contains colombia.open.build
def index(req):
    sub, _ = req.META['HTTP_HOST'].split('.', 1)
    if sub == 'colombia':
        return HttpResponseRedirect("/inicio")
    else:
        return HttpResponseRedirect("/")




class SignatureCreateView(CreateView):
    model = Signature
    template_name = 'home/signature.html'
    success_url = '/'  # Replace with the desired URL
    form_class = SignatureForm

    def form_valid(self, form):
        
        form.save()
        messages.success(self.request, 'Success, Your Signature has been Submitted!')
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
