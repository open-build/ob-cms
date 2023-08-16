from django.db import models
from django.contrib import admin

from wagtail.core.models import Page


class HomePage(Page):
    pass

class AboutPage(Page):
    pass

class Portfolio(Page):
    pass

class Foundry(Page):
    pass

class Radical(Page):
    pass

class Ethical(Page):
    pass

class Contact(Page):
    pass

class Inicio(Page):
    pass

class Nosotros(Page):
    pass

class Portafolio(Page):
    pass

class Programs(Page):
    pass

class Novedades(Page):
    pass

class Fundidora(Page):
    pass

class Ukraine(Page):
    pass

class Signature(models.Model):
    FRAMEWORK_CHOICES = [
        ('Radical', 'Radical'),
        ('Ethical', 'Ethical'),
        ('All', 'All'),
    ]

    linkedin_url = models.URLField(null=True, blank=True, help_text="Share your LinkedIn Profile")
    twitter_url = models.URLField(null=True, blank=True, help_text="Share your Twitter Profile")
    github_url = models.URLField(null=True, blank=True, help_text="Share your Github Profile")
    framework = models.CharField(max_length=10, choices=FRAMEWORK_CHOICES)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255,null=True, blank=True)
    is_collaborator = models.BooleanField(default=False,help_text="Check here if you would like to collaborate via GitHub")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SignatureAdmin(admin.ModelAdmin):
    list_display = ('company','name','email','framework')
    search_fields = ('company','name','email','framework')
    list_filter = ('company','name','email','framework')
    display = 'User Submitted Signature'