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
   
   
def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))


def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")


# def capfirst(request):
#     return HttpResponse("Capitalized First")

# def newlineremove(request):
#     return HttpResponse("New line remove")


# def spaceremove(request):
#     return HttpResponse("Space Remove <a href ='/'>back</a>")


# def charcount(request):
#     return HttpResponse("Charcount")