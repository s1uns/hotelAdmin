from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        authentication_form=LoginForm),
         name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout')

]