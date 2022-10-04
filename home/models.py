from django.db import models

from wagtail.core.models import Page

from modelcluster.fields import ParentalKey


class HomePage(Page):
    pass

class DevelopersPage(Page):
    pass

class AboutPage(Page):
    pass

class Foundry(Page):
    pass

class Contact(Page):
    pass
