from django.http import HttpRequest
from django.template import loader
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from HEAD.apps.students.models import StudentData
from .forms import UpdateForm

def update_status(request):
    # this page should only be accessed by a student so make check here
    if request.user.is_authenticated:
        current_user = StudentData.objects.get(id = 2)
        print(request.user.id)
       
        #right now im getting user with id 1 by default but you should get the id of
        #the student that is logged in
        # current_user = StudentData.objects.get(id = request.user.id)
        # but that data is fucked because your StudentData model is independent from the users
        # so you need to add the user to the model itself
        form = UpdateForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
        return render(request, 'blank.html', {'form':form})



    
    
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