from django.shortcuts import render
from .models import Website,Tag

# Create your views here.

def index(request):
    return render(request,'tagfind/index.html')

def find_tags(request):
    