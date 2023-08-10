from django.db import models

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

    linkedin_url = models.URLField()
    twitter_url = models.URLField()
    framework = models.CharField(max_length=10, choices=FRAMEWORK_CHOICES)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.url