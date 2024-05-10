from datetime import timedelta, timezone
from urllib import request
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from datetime import *
from django.utils import timezone
from application.models import Inhabitant, Premise, Premise_Inhabitant
from hotelAdmin import settings
from .forms import SignupForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from alerts_in_ua import Client as AlertsClient
import os



def home(request): 
    
    available_premises = Premise.objects.filter(premise_inhabitant=None)
    premise_inhabitants = Premise_Inhabitant.objects.all()
    context={'available_premises': available_premises, "premise_inhabitants": premise_inhabitants}
    return render(request, "premiseManagement.html", context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect('/')
    
@csrf_exempt    
def check_in_inhabitant(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        if(len(first_name) == 0):
            first_name = "Unnamed"
        
        last_name = request.POST.get('last_name')
        if(len(last_name) == 0):
            last_name = "User"
        premise_id = request.POST.get('premise')
        check_in_date = request.POST.get('check_in_date')
        if not check_in_date or timezone.make_aware(datetime.strptime(check_in_date, '%Y-%m-%d')) < timezone.now():
            check_in_date = timezone.now()
        else:
            check_in_date = timezone.make_aware(datetime.strptime(check_in_date, '%Y-%m-%d'))

        check_out_date = request.POST.get('check_out_date')
        if not check_out_date or timezone.make_aware(datetime.strptime(check_out_date, '%Y-%m-%d')) < check_in_date:
            check_out_date = check_in_date + timedelta(1)
        else:
            check_out_date = timezone.make_aware(datetime.strptime(check_out_date, '%Y-%m-%d'))

        inhabitant = Inhabitant.objects.create(first_name=first_name, last_name=last_name)
        premise = Premise.objects.get(id=premise_id)

        premise_inhabitant = Premise_Inhabitant.objects.create(
            premise=premise,
            inhabitant=inhabitant,
            checkIn_date=check_in_date,
            checkOut_date=check_out_date
        )

        return redirect('success-in')
    else:
        pass

def check_out(request, premise_inhabitant_id):
    premise_inhabitant = Premise_Inhabitant.objects.get(pk=premise_inhabitant_id)
    inhabitant = premise_inhabitant.inhabitant
    premise_inhabitant.delete()
    inhabitant.delete()
    return redirect('success-out')

def get_alarm(request, region_id=0):
    token = settings.API_TOKEN
    alarm_message = ''
    if(region_id != 0):
        token = os.getenv("API_TOKEN")
        alerts_client = AlertsClient(token=token)
        alert_status = alerts_client.get_air_raid_alert_status(region_id)

    return JsonResponse(alert_status.__str__(), status=200, safe=False)



class SuccessCheckInView(TemplateView):
    template_name = 'successedCheckIn.html'

class SuccessCheckOutView(TemplateView):
    template_name = 'successedCheckOut.html'