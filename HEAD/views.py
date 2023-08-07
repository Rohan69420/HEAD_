from django.http import HttpRequest, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from HEAD.apps.students.models import StudentData,studentStatus
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm,UpdateStatusForm,AddNewUserForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

# def errorPageHandler(request, exception):
#     return render(request, "404.html", status=404)


def user_authentication_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.success(request, ("There was an error loggin in. Try Again"))
            return redirect("newlogin")
    else:
        return render(request, "login.html", {})


def update_status(request):
    if request.user.is_authenticated:
        if PrivilegeChecker(request, "Student"):
            stdData = StudentData.objects.all().values()
            if not studentStatus.objects.filter(student = request.user).exists():
                 current_user_status = studentStatus(student = request.user )
                 current_user_status.save()
            else:
                current_user_status = studentStatus.objects.get(student = request.user)
            form = UpdateStatusForm(request.POST or None, instance=current_user_status)
            if form.is_valid():
                form.save()
                return render(request, 'blank.html', {'form':form})
            else:
                return render(request, 'blank.html', {'form':form})
            
        else:
            return HttpResponseRedirect(reverse('error404'))
    else:
        return HttpResponseRedirect(reverse("newlogin"))


def show_tables(request):
    if request.user.is_authenticated:
        stdData = StudentData.objects.all()
        if PrivilegeChecker(request, "Teacher"):
            return render(
                request,
                "tables.html",
                {
                    "stdData": stdData,
                    "group": request.user.groups.all().values()[0]["name"],
                },
            )
        else:
            return HttpResponseRedirect(reverse('error404'))
    else:
        return HttpResponseRedirect(reverse("accounts:login"))  # redirect to login page


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


def DashboardView(request):
    print("Hello")
    print(request.user.groups.all().values())
    if request.user.is_authenticated:
        return render(
            request,
            "index.html",
           {"group": request.user.groups.all().values()[0]["name"]},
        )
    else:
        return redirect("newlogin")


def PrivilegeChecker(request, group):
    if request.user.groups.all().values()[0]["name"] == group or request.user.is_superuser :
        print("PRivilege checker")
        return True
    else:
        return False
        print("Error404")
        return HttpResponseRedirect(reverse("error404"))


#admin adding new user
def admin_add_user(request):
    if request.user.is_authenticated:
        if PrivilegeChecker(request, "Admin"):
                if request.method == "GET":
                        form = AddNewUserForm()
                        return render(request, 'addUser.html', {'form':form})
                else :
                        form = AddNewUserForm(request.POST)
                        print(form.errors.as_data())
                        if form.is_valid():
                            form_data = form.cleaned_data

                            new_user = User.objects.create(
                                username=form_data["username"],
                                email=form_data["email"],
                            )
                            new_user.set_password("default123")
                            new_user.groups.add(form_data["group"])
                            new_user.save()
                            return render(request, 'addUser.html', {'form':form})
                        else:
                            return HttpResponse(str(form.errors), status=400)                                                       
        else:
            return HttpResponseRedirect(reverse('error404'))
    else:
        return HttpResponseRedirect(reverse("newlogin"))


# 404 error
def show404(request):
    return render(request, "404.html", {"group":request.user.groups.all().values()[0]["name"]})

def passwordReset(request):
    return render(request,"forgot-password.html",{})