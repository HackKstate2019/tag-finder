from django.shortcuts import render
from .models import Website,Tag

from .forms import UrlForm
from .nlp_nltk_processing_text import tags
from .compare import compare
from .exists_model_parser import exists_model_parser
from .database_test import print_test

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
            exists_model_parser(t) #Checks if Article is already in DB, if not then it makes a new Website and appends Tags to it.
            c=compare(t) #Compares Input Article to all of the Articles in the DB, forming Reference Ratings (RR) between each page.

            print('Compare\'s Output: ', c)
            print('Compare\'s [0]: ', c[0])
            print('Compare\'s [0][0]: ', c[0][0])
            print('Compare\'s Output Length: ', len(c))

            # return render(request, 'tagfind/landing.html', {'form':form})

            #This is expecting the actual information to just be passed on.
            titlevar1=c[0][1]
            siteurl1=c[0][0]
            rr1=c[0][2]

            titlevar2=c[1][1]
            siteurl2=c[1][0]
            rr2=c[1][2]

            titlevar3=c[2][1]
            siteurl3=c[2][0]
            rr3=c[2][2]

            #This is expecting the website's ID, not the actual information.
            # titlevar1=Website.objects.filter(id=int(c[0][0])).values('title')
            # siteurl1=Website.objects.filter(id=int(c[0][0])).values('url')
            # rr1=str(c[0][1])
            # try:
            #     titlevar2=Website.objects.filter(id=int(c[1][0])).values('title')
            #     siteurl2=Website.objects.filter(id=int(c[1][0])).values('url')
            #     rr2=str(c[1][1])
            #     titlevar3=Website.objects.filter(id=int(c[2][0])).values('title')
            #     siteurl3=Website.objects.filter(id=int(c[2][0])).values('url')
            #     rr3=str(c[2][1])
            # except:
            #     titlevar2=''
            #     siteurl2=''
            #     rr2=''
            #     titlevar3=''
            #     siteurl3=''
            #     rr3=''

            searchedtitle=t[0][1]
            searchedurl=t[0][0]
            
            return render(request, 'tagfind/landing.html', {'form':form,'titlevar1':titlevar1,
                                    'titlevar2':titlevar2,'titlevar3':titlevar3,
                                    'siteurl1':siteurl1,'siteurl2':siteurl2,
                                    'siteurl3':siteurl3,'searchedtitle':searchedtitle,
                                    'searchedurl':searchedurl,'rr1':rr1,'rr2':rr2,'rr3':rr3})

    else: #If it's a GET method
        form = UrlForm() #Provides empty Form Class in the form of HTML (see index.html)
        
    return render(request, 'tagfind/index.html', {'form':form})
    