from django.contrib import messages
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from classes.models import Course, Guest, Notification, Result


# Create your views here.
def index(request):

    notifications = Notification.objects.all()
    courses = Course.objects.all()
    mediums = Result.med_choices
    subjects = Result.sub_choices
    stds = Result.std_choices
   
    context = {
        "notifications" : notifications,
        "courses" : courses,
        "mediums" : mediums,
        "subjects" : subjects,
        "stds" : stds
    }
    return render(request,'index.html',context)

def results(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed..!")
    else :
        try :
            medium = request.POST.get('medium')
            sub = request.POST.get('subject')
            std = request.POST.get('std')

            results = Result.objects.filter(medium=medium,sub=sub,std=std)
            
            mediums = Result.med_choices
            subjects = Result.sub_choices
            stds = Result.std_choices
            context = {
                "mediums" : mediums,
                "subjects" : subjects,
                "stds" : stds,
                "results" : results
            }
            return render(request,'results.html',context)
        except :
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
