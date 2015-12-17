from django.shortcuts import render
from django.http import HttpResponse
from show.models import data1
from show.models import rid_table
# Create your views here.

def index(request):
    ctx=rid_table.objects.all()
    return render(request,'show/index.html',{'rid_table':ctx})
def about(request):
    ctx=rid_table.objects.all()
    return render(request,'show/about.html',{'rid_table':ctx})
