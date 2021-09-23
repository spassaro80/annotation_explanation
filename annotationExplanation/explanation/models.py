from django.db import models

# Create your models here.

class Donor(models.Model):

    # Gender Choices
    SEX_CHOICES = (
        ('M', 'Maschio'),
        ('F', 'Donna'),
        ('O', 'Other'),
    )

    # Language choices
    LANG_CHOICES = (
        ('IT', 'Italiano'),
        ('DE', 'Tedesco'),
        ('FR', 'Francese'),
        ('EN', 'Inglese'),
    )

    company = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, unique = True, null=True)
    mobile_phone = models.CharField(max_length=15, blank=True, null=True)
    private_phone = models.PositiveIntegerField(blank=True, null=True)
    office_phone = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    address2 = models.TextField(max_length=200, blank=True, null=True)
    postal_box = models.CharField(max_length=50, blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANG_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.CharField(max_length=50, blank=False)

    def __str__(self):
       return self.first_name + " " + self.last_name

class Donation(models.Model):

    # Currency Choices
    CURRENCY_CHOICES = (
        ('CHF', 'FRANCO'),
        ('EUR', 'EURO'),
        ('USD', 'DOLLARO'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    donor = models.ForeignKey('donor', on_delete=models.CASCADE, related_name='donations')
    amount = models.FloatField(blank=False)
    currency = models.CharField(max_length=3, choices = CURRENCY_CHOICES)
    cost_center = models.CharField(max_length=200, blank=True, null=True)
    added_by = models.CharField(max_length=50, blank=False)

    def __str__(self):
       return str(self.donor)
