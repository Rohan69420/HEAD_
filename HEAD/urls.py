"""
URL configuration for HEAD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DashboardView),
    path('table',views.show_tables,name='table'),
    path('update',views.update_status,name='update'),
    path('dashboard',views.DashboardView,name="dashboard"),
    path('newlogin',include('django.contrib.auth.urls')),
    path('newlogin/login',views.user_authentication_login,name="newlogin"),
    path('logout',auth_views.LogoutView.as_view(),name='newlogout'),
    path('error404',views.show404,name="error404"),
    path('reset',views.passwordReset,name="reset")
]
urlpatterns += staticfiles_urlpatterns()

#path('accounts/', include('django.contrib.auth.urls'))