from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from app.models import Profile 

def home(request):
    tabcontents = [
        {'urlname': 'home'},
        {'urlname': 'temp_tutorial'},
        {'urlname':'modeltut'},
        
    ]
    return render(request,'home.html', {'tabcontents': tabcontents})

def template_tutorial(request):
    todaydate= datetime.now()
    someone={'name':'Abhinav','num':24.03421,'city':'jabalpur','desc':'hello My name is abhinav sahu and I am from Jabalpur','date':todaydate}
    return render(request,'app/TemplateTutorial.html',context = someone)

def models_tutorial(req):
    stu_profile=Profile.objects.all()
    print(stu_profile)
    return render(req,'app/modelstut.html',{'students':stu_profile})