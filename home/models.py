from django.db import models
from datetime import timedelta
from decimal import Decimal
import uuid

from django.contrib import admin
from django.utils import timezone

from wagtail.core.models import Page

from modelcluster.fields import ParentalKey


class HomePage(Page):
    pass

class AboutPage(Page):
    pass

class Foundry(Page):
    pass

class Contact(Page):
    pass

class Community(Page):
    pass

class ContactMail(models.Model):
    name = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    email = models.CharField(max_length=255, blank=True)
    file = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def clean_email(self):
        original_email = self.cleaned_data.get('email')

        if "@" not in original_email:
            raise ValidationError("Invalid Email address")

        if "." not in original_email:
            raise ValidationError("Invalid Email address")

        return original_email

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(ContactMail, self).save(*args, **kwargs)



class ContactMailAdmin(admin.ModelAdmin):
    list_display = ('name','email','url','create_date','edit_date')
    search_fields = ('name','email')
    list_filter = ('name',)
    display = 'Contact Form'
