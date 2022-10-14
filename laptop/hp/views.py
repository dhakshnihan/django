from django.http import HttpResponse

# Create your views here.
def shirt(request):
    return HttpResponse('this is shirt')
def pant(request):
    return HttpResponse('this is pant')