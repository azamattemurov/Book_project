from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    b = Book.objects.all()
    return render(request,'templates/index.html',context={'books':b})
