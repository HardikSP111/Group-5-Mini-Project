#I have created this file - Om bhoge

#Code for video #6(codewithharry)

from django.http import HttpResponse
from django.shortcuts import render
#def index(request) : 
 #   return HttpResponse('''<h1>Om</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django Code With Om</a>''')

#def about(request) : 
 #   return HttpResponse("About hello om")
 
# Code For Video #7 

def index(request):
    return render(request,'index.html')
   # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    analyzed = djtext
    params = {'purpose' : 'Removed punctuation' , 'analyzed text' : 'Analyzed text'}
    #Analyze the text
    return render(request , 'analyze.html' , 'off')

# def capfirst(request):
#     return HttpResponse("Capitalized First")

# def newlineremove(request):
#     return HttpResponse("New line remove")


# def spaceremove(request):
#     return HttpResponse("Space Remove <a href ='/'>back</a>")


# def charcount(request):
#     return HttpResponse("Charcount")