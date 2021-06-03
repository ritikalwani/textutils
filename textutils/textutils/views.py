# created by Ritik

from django.http import HttpResponse
from django.shortcuts import render


# code for links


def index(request):
    return render(request, 'index.html')



def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    countchar=request.POST.get('countchar','off')
    para={}
    temp_text=djtext
    bl=False

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\/,<>?@#$%^&*_.'''
        analyzed = ""
        for char in temp_text:
            if char not in punctuations:
                analyzed = analyzed + char
        bl=True
        temp_text=analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in temp_text:
            analyzed = analyzed + char.upper()

        bl = True
        temp_text=analyzed

    if newlineremove=='on':
        analyzed=""
        for char in temp_text:
            if char!='\n' and char!='\r':
                analyzed+=char
        bl = True
        temp_text=analyzed
    if extraspaceremove=='on':
        analyzed=""
        temp_text=' '.join(temp_text.split())
        for index,char in enumerate(temp_text):
            if (djtext[index]==" ") and djtext[index+1]==" ":
                pass
            else:
                analyzed+=char
        bl = True
        temp_text=analyzed
    if countchar=='on':
        analyzed=""
        count=0
        for char in temp_text:
            count=count+1
        analyzed=temp_text +" Total "+str(count)+" characters."
        bl = True
        temp_text=analyzed

    if bl==True:
        para={'analyzed_text': temp_text}
        return render(request,'analyze.html',para)



    else:
        return HttpResponse("Error")

