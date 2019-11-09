from django.shortcuts import render
from .models import Website,Tag

from .forms import UrlForm

# Create your views here.

def index(request):
    form = UrlForm() #Gives index.html an empty form to input URL.
    return render(request,'tagfind/index.html',{'form':form})

def find_tags(request,url):
    return render(request, '')

def get_url(request):
    if request.method=='POST':
        form = UrlForm(request.POST) #Assigns filled out Form Class to variable 'form'

        if form.is_valid(): #.cleaned_data puts the Form info into a dictionary
            titlevar1='Billy'
            siteurl1=form
            titlevar2=form.cleaned_data['url']
            siteurl2=form
            titlevar3=form
            siteurl3=form

            searchedtitle=form
            searchedurl=form

            return render(request, 'tagfind/landing.html', {'form':form,'titlevar1':titlevar1,'titlevar2':titlevar2,'titlevar3':titlevar3,'siteurl1':siteurl1,'siteurl2':siteurl2,'siteurl3':siteurl3,'searchedtitle':searchedtitle,'searchedurl':searchedurl})

    else: #If it's a GET method
        form = UrlForm() #Provides empty Form Class in the form of HTML (see index.html)
        
    return render(request, 'tagfind/index.html', {'form':form})
    