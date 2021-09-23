from django.contrib import admin
from .models import Donor, Donation

class DonorAdmin(admin.ModelAdmin):
    model =  Donor
class DonationAdmin(admin.ModelAdmin):
    model =  Donation

admin.site.register(Donor, DonorAdmin)
admin.site.register(Donation, DonationAdmin)