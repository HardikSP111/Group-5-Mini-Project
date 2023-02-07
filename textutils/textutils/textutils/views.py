#I have created this file - Om bhoge

#Code for video #6(codewithharry)

from django.http import HttpResponse

#def index(request) : 
 #   return HttpResponse('''<h1>Om</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django Code With Om</a>''')

#def about(request) : 
 #   return HttpResponse("About hello om")
 
# Code For Video #7 

def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("Remove Punc")

def capfirst(request):
    return HttpResponse("Capitalized First")

def newlineremove(request):
    return HttpResponse("Newlineremove")


def spaceremove(request):
    return HttpResponse("SpaceRemove")


def charcount(request):
    return HttpResponse("Charcount")