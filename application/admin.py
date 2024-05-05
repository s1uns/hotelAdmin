from django.contrib import admin

from application.models import Inhabitant, Premise, Premise_Inhabitant

# Register your models here.
admin.site.register(Premise)
admin.site.register(Inhabitant)
admin.site.register(Premise_Inhabitant)