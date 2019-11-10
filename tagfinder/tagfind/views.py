from django.shortcuts import render
from .models import Website,Tag

from .forms import UrlForm
from .nlp_nltk_processing_text import tags
from .compare import compare

# Create your views here.

def index(request):
    form = UrlForm() #Gives index.html an empty form to input URL.
    return render(request,'tagfind/index.html',{'form':form})

def page_check(request,url):
    return render(request, '')

def get_url(request):
    if request.method=='POST':
        form = UrlForm(request.POST) #Assigns filled out Form Class to variable 'form'

        if form.is_valid(): #.cleaned_data puts the Form info into a dictionary
            t=tags(form.cleaned_data['url']) #url, title, tag&value
            c=compare(t)

            titlevar1=c[0][1]
            siteurl1=c[0][0]
            titlevar2=c[1][1]
            siteurl2=c[1][0]
            titlevar3=c[2][1]
            siteurl3=c[2][0]

            searchedtitle=t[0][1]
            searchedurl=t[0][0]
            
            return render(request, 'tagfind/landing.html', {'form':form,'titlevar1':titlevar1,'titlevar2':titlevar2,'titlevar3':titlevar3,'siteurl1':siteurl1,'siteurl2':siteurl2,'siteurl3':siteurl3,'searchedtitle':searchedtitle,'searchedurl':searchedurl})

    else: #If it's a GET method
        form = UrlForm() #Provides empty Form Class in the form of HTML (see index.html)
        
    return render(request, 'tagfind/index.html', {'form':form})
    