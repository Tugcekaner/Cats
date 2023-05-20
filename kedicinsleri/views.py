from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    kediCinsler=KediCins.objects.all
    context={
        'kedicinsleri':kediCinsler
    }
    return render(request,'index.html',context)

def detail(request,kediId):
    kedi=KediCins.objects.get(id=kediId)
    context={
        'kedi':kedi
    }
    return render(request,'detail.html',context)