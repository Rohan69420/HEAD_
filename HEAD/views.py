from django.http import HttpRequest
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    print(request.user)
    return render(request,'index.html')
    #template = loader.get_template('index.html')
    #return HttpRequest(template.render({}, request))

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'