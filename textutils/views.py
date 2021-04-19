# Self created file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def analyze(request):
    send=""
    djtext = request.POST.get('text','NoText')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')
    punctuations='''!(){},.;:'"?[]\|/-_@#$%^&*()<>|='''

    if removepunc =='on':
        analyzed=""
        for i in djtext:
            if i in punctuations:analyzed+=" "
            else:analyzed+=i
        djtext=analyzed

    if fullcaps == 'on':
        analyzed =''
        for i in djtext:
            analyzed+=i.upper()
        djtext=analyzed

    if newlineremover == 'on':
        analyzed=""
        for i in djtext:
            if i != "\n" and i!="\r":analyzed+=i
        djtext=analyzed

    if extraspaceremover == 'on':
        analyzed=''
        for i,char in enumerate(djtext):
            if i<len(djtext)-1:
                if djtext[i]==' ' and djtext[i+1]==' ': continue
                else:analyzed+=char
        djtext=analyzed

    if charcounter=='on':
        count=len(djtext)
        send=str(count)+" Characters"
        
    params = {'analyzed_text':djtext,'counts':send}
    return render(request,'analyze.html',params)

