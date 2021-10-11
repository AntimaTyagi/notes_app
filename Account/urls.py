from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib.auth.views import LoginView,LogoutView
from .import views
from .views import RegisterView
app_name="account"

urlpatterns = [
   
    path("login/",LoginView.as_view(template_name="account/login.html"),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("register/",views.RegisterView,name="register")
]


