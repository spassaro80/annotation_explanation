from django.shortcuts import render
from .models import Donor, Donation
from django.db.models import Sum

# Create your views here.

def donatori(request):
    donordata = Donor.objects.annotate(tot_donations = Sum('donations__amount'))
    context = {'donor': donordata}
    return render(request, 'donors.html', context)

#count donations
# Donor.objects.annotate(tot_donations = Sum('donations__amount'), num_donations = Count('donations'))

#last year donations

# Donor.objects.filter(donations__cost_center = "2019").annotate(tot_donations = Sum('donations__amount'))

# donations per year
# Donor.objects.values('donations__cost_center').annotate(tot_per_year = Sum('donations__amount'))

#donations per year and donor: 
# Donation.objects.values('donor').values('cost_center', 'donor').annotate(tot_per_year = Sum('amount'))