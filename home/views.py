from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect

#redirect to spanish if the url contains colombia.open.build
def index(req):
    sub, _ = req.META['HTTP_HOST'].split('.', 1)
    if sub == 'colombia':
        return HttpResponseRedirect("/inicio")
    else:
        return HttpResponseRedirect("/")
