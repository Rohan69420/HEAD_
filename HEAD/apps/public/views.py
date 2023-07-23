from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    print(request.user)
    return render(request,'index.html')
    #template = loader.get_template('index.html')
    #return HttpRequest(template.render({}, request))

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
# Create your views here.
