from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    pass

class AboutPage(Page):
    pass

class ArtistsPage(Page):
    pass

class SubmitPage(Page):
    pass