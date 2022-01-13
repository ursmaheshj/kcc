from django.contrib import messages
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from classes.models import Course, Guest, Result


# Create your views here.
def index(request):
    courses = Course.objects.all()
    stds = Result.std_choices
    context = {
        "courses" : courses,
        "stds" : stds
    }
    return render(request,'index.html',context)

def results(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        #try :
            medium = Course.objects.get(title=request.POST.get('medium'))
            std = request.POST.get('std')

            results = Result.objects.filter(std=std,medium=medium.id)
            
            courses = Course.objects.all()
            stds = Result.std_choices
            context = {
                "courses" : courses,
                "stds" : stds,
                "results" : results
            }
            return render(request,'results.html',context)
        #except :
            messages.error(request,"Something went wrong please try again")
            return HttpResponseRedirect("results")

def addguest(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        try :
            name = request.POST.get('name')
            email = request.POST.get('email')
            sub = request.POST.get('subject')
            message = request.POST.get('message')

            guest = Guest.objects.create(name=name,email=email,sub=sub,message=message)
            guest.save()
            
            messages.success(request,"Your details sent successfully")
            return HttpResponseRedirect("/#contact")
        except :
            messages.error(request,"Failed to send details")
            return HttpResponseRedirect("/#contact")
