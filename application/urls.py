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
    path('logout/', views.logout_view, name='logout'),
    path('check-in/', views.check_in_inhabitant, name='check-in'),
    path('check_out/<int:premise_inhabitant_id>/', views.check_out, name='check_out'),
    path('success-in/', views.SuccessCheckInView.as_view(), name='success-in'),
    path('success-out/', views.SuccessCheckOutView.as_view(), name='success-out'),

]