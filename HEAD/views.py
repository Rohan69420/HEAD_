from django.http import HttpRequest
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from HEAD.apps.students.models import StudentData
from .forms import UpdateForm

def update_status(request):
    stdData=StudentData.objects.all()
    return render(request,'blank.html',{'stdData':stdData})

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