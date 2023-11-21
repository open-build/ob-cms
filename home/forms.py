from .models import Signature, MentorApplication, ProjectSubmission
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
        fields = ['name', 'email', 'company', 'framework', 'company','linkedin_url', 'twitter_url','github_url','is_collaborator']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))


class MentorApplicationForm(forms.ModelForm):
    class Meta:
        model = MentorApplication
        fields = ['name', 'email', 'linkedin_profile', 'resume', 'application_type', 'experience']

    def __init__(self, *args, **kwargs):
        super(MentorApplicationForm, self).__init__(*args, **kwargs)
        self.fields['resume'].required = False


class ProjectSubmissionForm(forms.ModelForm):
    class Meta:
        model = ProjectSubmission
        fields = ['submitter_name', 'submitter_email', 'project_title', 'project_description']

