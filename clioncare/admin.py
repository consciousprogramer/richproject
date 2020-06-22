from django.contrib import admin
from .models import patient,usermessage,add_offer
# Register your models here.
admin.site.register(patient)
admin.site.register(usermessage)
admin.site.register(add_offer)
