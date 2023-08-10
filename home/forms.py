from .models import Signature
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from crispy_forms.layout import Layout, Submit, Reset, Div, HTML, Fieldset, Field
from functools import partial
from django import forms
from django.urls import reverse


import os

import requests


class SignatureForm(forms.ModelForm):
    
    class Meta:
        model = Signature
        fields = ['linkedin_url', 'twitter_url', 'name', 'email', 'company', 'framework', 'company']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))
        
