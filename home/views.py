from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect

#redirect to spanish if the url contains colombia.open.build
def index(request):
    if request.META['HTTP_HOST'] is "colombia.open.build":
        homepage="/inicio"
    else:
        homepage="/"
    return HttpResponseRedirect(homepage)
