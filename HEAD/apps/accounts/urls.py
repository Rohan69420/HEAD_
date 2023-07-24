from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name="accounts"
urlpatterns = [
    path('profile',views.ProfileView.as_view(),name='profile'),

    #Django Auth
    path('login',auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout',auth_views.LogoutView.as_view(),name='logout')
]

#path('accounts/', include('django.contrib.auth.urls'))