from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.conf.urls import url
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from puput import urls as puput_urls
from home.views import SignatureCreateView, apply_to_mentor, submit_project  # Import your new views here

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('search/', search_views.search, name='search'),

    url(r'^signature/$', SignatureCreateView.as_view(), name='signature'),

    path('apply-to-mentor/', apply_to_mentor, name='apply-to-mentor'),  # New URL pattern for mentor application
    path('apply-as-student/', apply_to_mentor, name='apply-as-student'),  # New URL pattern for mentor application
    path('submit-project/', submit_project, name='submit-project'),  # New URL pattern for project submission

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(puput_urls)),
    path("", include(wagtail_urls)),
    path('__debug__/', include('debug_toolbar.urls')),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
