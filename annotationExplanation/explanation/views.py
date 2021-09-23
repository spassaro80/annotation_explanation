from django.shortcuts import render
from .models import Donor, Donation
from django.db.models import Sum

# Create your views here.

def donatori(request):
    donordata = Donor.objects.annotate(tot_donations = Sum('donations__amount')).order_by('tot_donations')
    context = {'donor': donordata}
    return render(request, 'donors.html', context)

    #Inutile attualmente
    # donation_donor = Donation.objects.values('donor_id')
    #Inutile attualmente
    # donation_count = Donation.objects.values('donor_id').annotate(total=Sum('amount'))
