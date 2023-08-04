from django.http import HttpRequest
from django.template import loader
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from HEAD.apps.students.models import StudentData
from .forms import UpdateForm
from django.contrib.auth import login

def update_status(request):
    
    if request.user.is_authenticated:
        # this page should only be accessed by a student so make check here
        current_user = StudentData.objects.get(id = 2)
        #print(request.user.id)
       
        # right now im getting user with id 1 by default but you should get the id of
        # the student that is logged in

        # current_user = StudentData.objects.get(id = request.user.id)

        # but that data is fucked because your StudentData model is independent from the users
        # so you need to find out which user is logged in 
        # ( which would have been easy if the StudentData model was already related to the Users)
        # check models for that ive added an example
        # but i guess you have to do code in some loop check to check which user is currently logged in
        # and match that student to their status
         
        form = UpdateForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            return render(request, 'blank.html', {'form':form})
        # make this go back to the users profile page or somewhere else
        # doing that might log out the user so add this line after form.save()
        # login(request, current_user)
        # login needs to be imported (check top)
        else:
            return render(request, 'blank.html', {'form':form})
        # show an error message saying form is invalid



    
    
def index(request):
    print(request.user)
    return render(request,'index.html')
    #template = loader.get_template('index.html')
    #return HttpRequest(template.render({}, request))

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def show_tables(request):
    stdData = StudentData.objects.all()
    return render(request,'tables.html',{'stdData':stdData})

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'