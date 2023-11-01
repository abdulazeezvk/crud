from django.shortcuts import render, redirect
from .models import Course


from myapp.forms import LoginForm, UserRegistrationForm
from django.contrib.auth import login, authenticate
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
        return redirect("myapp:showdata")

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



#create a login

def account(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        form = LoginForm(request.POST)
        
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('account')
        # Note: You can use 'elif' instead of 'if' here
        elif form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])  # Fix password retrieval
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'main/crudstart.html', {'form': form})
            else:
                return render(request, 'main/crudstart.html', {'form': form})
    else:
        user_form = UserRegistrationForm()
        form = LoginForm()
            
    return render(request,'main/crudstart.html', {'user_form': user_form, 'form': form})  # Pass both forms to the template

    #return render(request,'main/crudstart.html')