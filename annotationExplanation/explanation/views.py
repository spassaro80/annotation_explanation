from django.shortcuts import render
from .models import Donor, Donation
from django.db.models import Sum

# Create your views here.

def donatori(request):
    donordata = Donor.objects.annotate(tot_donations = Sum('donations__amount'))
    donors_2019 = Donor.objects.filter(donations__cost_center = "2019").annotate(tot_2019 = Sum('donations__amount')).values()
    donors_dict = donordata.values()
    for donor in donors_dict:
        if donors_2019.filter(id=donor['id']).exists():
            donor['tot_2019'] = donors_2019.filter(id=donor['id']).values()[0]['tot_2019']
        else:
            donor['tot_2019'] = 0

    context = {'donor': donorsdict}
    return render(request, 'donors.html', context)

#count donations
# Donor.objects.annotate(tot_donations = Sum('donations__amount'), num_donations = Count('donations'))

#last year donations

# Donor.objects.filter(donations__cost_center = "2019").annotate(tot_donations = Sum('donations__amount'))

# donations per year
# Donor.objects.values('donations__cost_center').annotate(tot_per_year = Sum('donations__amount'))

#donations per year and donor: 
# Donation.objects.values('donor').values('cost_center', 'donor').annotate(tot_per_year = Sum('amount'))

#donations per year with 0 sum

# donors_2019 = Donor.objects.filter(donations__cost_center = "2019").annotate(tot_2019 = Sum('donations__amount')).values()
# donors_dict = donordata.values()
# for donor in donors_dict:
#     if donors_2019.filter(id=donor['id']).exists():
#         donor['tot_2019'] = donors_2019.filter(id=donor['id']).values()[0]['tot_2019']
#     else:
#         donor['tot_2019'] = 0

# context = {'donor': donorsdict}
# return render(request, 'donors.html', context)