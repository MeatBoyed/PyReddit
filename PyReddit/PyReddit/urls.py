from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as authViews
from users.views import registerPage 
from reddit.views import homePage

urlpatterns = [
    path("", homePage, name="homePage"),
    path("register/", registerPage, name="user-register"),
    path("login/", authViews.LoginView.as_view(template_name="users/loginPage.html"), name="user-login"),
    path("logout/", authViews.LogoutView.as_view(template_name="users/logoutPage.html"), name="user-logout"),
    path('admin/', admin.site.urls),
]
