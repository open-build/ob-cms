from django import forms
from  .models import ContactMail


class ContactMailForm(forms.ModelForm):
    file = forms.FileField(required=False)

    class Meta:
        model = ContactMail

        fields = ('name','email','url','message','file')

        widgets = {
            'message':forms.Textarea(attrs={'cols':10,'rows':3})
        }
        labels = {
            'name':'Full Name'
        }
