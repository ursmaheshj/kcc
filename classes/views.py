from django.contrib import messages
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from classes.models import Guest, Result


# Create your views here.
def index(request):
    return render(request,'index.html')

def results(request):
    results = Result.objects.all()
    return render(request,'results.html',{'results':results})

def home(request):
    return render(request,'admin/ahome.html',{'results':results})

def addguest(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        #try :
            name = request.POST.get('name')
            email = request.POST.get('email')
            sub = request.POST.get('subject')
            message = request.POST.get('message')

            guest = Guest.objects.create(name=name,email=email,sub=sub,message=message)
            guest.save()
            
            messages.success(request,"Your details sent successfully")
            return HttpResponseRedirect("/")
        #except :
            messages.error(request,"Failed to send details")
            return HttpResponseRedirect("/#contact")
