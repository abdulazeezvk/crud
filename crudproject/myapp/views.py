from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    return render(request,'main/index.html')


def showdata(request):
    data=Course.objects.all()
    print(data)
    context={"data":data}
    
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        instructor=request.POST.get('instructor')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        capacity=request.POST.get('capacity')

        query=Course(title=title,description=description,instructor=instructor,start_date=start_date,end_date=end_date,capacity=capacity)
        query.save()
        return redirect("/")
    return render(request,'main/show.html',context)
     
def updatedata(request,id):
     if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        instructor=request.POST['instructor']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        capacity=request.POST['capacity']

        update=Course.objects.get(id=id)
        update.title=title
        update.description=description
        update.instructor=instructor
        update.start_date=start_date
        update.end_date=end_date
        update.capacity=capacity
        update.save()
        return redirect("/show")
     d=Course.objects.get(id=id)
     context={"d":d}
     return render(request,'main/update.html',context)
     
def deletedata(request,id):
    d=Course.objects.get(id=id)
    d.delete()
    return redirect("/show")
    # return render(request,'main/index.html')