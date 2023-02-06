#I have created this file - Om bhoge
from django.http import HttpResponse

def index(request) : 
    return HttpResponse("<h1>Om</h1>")

def about(request) : 
    return HttpResponse("About hello om")