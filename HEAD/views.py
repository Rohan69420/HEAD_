from django.http import HttpRequest,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from HEAD.apps.students.models import StudentData
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm
from django.urls import reverse
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

def user_authentication_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.success(request, ("There was an error loggin in. Try Again"))
            return redirect('newlogin')
    else:
        return render(request, "login.html",{})

def update_status(request):
    stdData = StudentData.objects.all().values()
    if request.method == "GET":
        form = UpdateForm()
        return render(request, "blank.html", {"stdData": stdData, "form": form})
    else:
        form = UpdateForm(request.POST)
        # print(stdData)
        print("            ")
        form.is_valid()
        data = form
        for n in stdData:
           # print(n['id'])
           
            
            if n['id'] == request.user.id:
                hamroUser = StudentData.objects.get(pk = n["id"])
                #print(data["status"])
                hamroUser.status_id = int(request.POST["status"])
                print(type(request.POST["status"]))
                #options = ["Pending","Accepted","Rejected","Unverified"]
                #gotData = options[request.POST["status"] - 1]
                #hamroUser.status = gotData

                print(hamroUser.status_id)
                hamroUser.save()
        return render(request, "blank.html", {"stdData": stdData})


def index(request):
    print(request.user)
    return render(request, "index.html")
    # template = loader.get_template('index.html')
    # return HttpRequest(template.render({}, request))


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def show_tables(request):
    if not request.user.is_authenticated: #if the user is not authenticated
        return HttpResponseRedirect(reverse("accounts:login")) #redirect to login page
    else:
        stdData = StudentData.objects.all()
        #print(type(stdData[0].professor.name))
        #print("----------------------------------------")
        return render(request, "tables.html", {"stdData": stdData})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"