from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from HEAD.apps.students.models import StudentData
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm, AddNewUserForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


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
            if not StudentData.objects.filter(student = request.user).exists():
                 current_user_status = StudentData(student = request.user )
                 current_user_status.save()
            else:
                current_user_status = StudentData.objects.get(student = request.user)
            form = UpdateForm(request.POST or None, instance=current_user_status)
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
        return HttpResponseRedirect(reverse("newlogin"))  # redirect to login page



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


# 404 error
def show404(request):
    return render(request, "404.html", {"group":request.user.groups.all().values()[0]["name"]})

def passwordReset(request):
    return render(request,"forgot-password.html",{})

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