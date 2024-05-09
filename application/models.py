from datetime import timedelta
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Premise(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name
    
class Inhabitant(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    
    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)
    

class Premise_Inhabitant(models.Model):
    premise = models.ForeignKey(Premise, on_delete=models.CASCADE)
    inhabitant = models.ForeignKey(Inhabitant, on_delete=models.CASCADE)
    checkIn_date = models.DateTimeField(default=timezone.now())
    checkOut_date = models.DateTimeField(default=timezone.now() + timedelta(1))

    def __str__(self):
        return '{inhabitant} checked-in the {premise} from {checkIn} till {checkOut}'.format(inhabitant=self.inhabitant.__str__(), premise=self.premise.__str__(),  checkIn=self.checkIn_date.strftime("%d %m %Y"), checkOut=self.checkOut_date.strftime("%d %m %Y"))