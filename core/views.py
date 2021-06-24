from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    about = About.objects.first()
    services = Service.objects.all()
    works = Work.objects.all()
    li=[]
    print("Skills Are : ",type(about.skill))
    for i in about.skill:
        li.append(i)
    
    return render(request,'index.html',{'about':about,'services':services,'works':works,'a':li[0],'b':li[1],'c':li[2]})
