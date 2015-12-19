from django.shortcuts import render
from django.http import HttpResponse
from show.models import data
from show.models import mode
# Create your views here.

def index(request):
    ctx=data.objects.all()
    return render(request,'show/index.html',{'rid_table':ctx})
def about(request):
    ctx=mode.objects.all()
    return render(request,'show/about.html',{'rid_table':ctx})
