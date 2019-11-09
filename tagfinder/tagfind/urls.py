from django.urls import path
from . import views

app_name='tagfind'

urlpatterns=[
    path('',views.index,name='index')
]