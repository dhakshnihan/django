from optparse import Values
from django.shortcuts import render
from apple.models import Tiru

# Create your views here.
def homepage(request):
    return render(request,'index.html')
def calm(request):
    Values={'name':'jyothi','age':24,'address':'vzg'}
    return render(request,'jyothi.html',Values)
def quit(request):
    result = Tiru.objects.all()
    jyo={'allresult':result}
    return render(request,'jyothi1.html',jyo)

