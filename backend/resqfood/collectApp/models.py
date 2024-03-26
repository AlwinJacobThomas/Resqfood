from django.db import models
from userApp.models import User
from phonenumber_field.modelfields import PhoneNumberField

class IndividualProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='individual_profile')
    # Add fields specific to individual profiles here
    address = models.TextField(null=True,blank=True)
    phone = PhoneNumberField(null=True)

class OrganizationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization_profile')
    verified = models.BooleanField(default=False)
    # Add fields specific to organization profiles here
    address = models.TextField(null=True,blank=True)
    phone = PhoneNumberField(null=True)
    website = models.URLField(null=True, blank=True)
    

class Location(models.Model):
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat  = models.DecimalField(max_digits=9, decimal_places=6)
    
class FoodRequest(models.Model):
    organization = models.ForeignKey(OrganizationProfile, on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    address = models.CharField(max_length=255)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateTimeField()
    # Add fields for meal types
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    MEAL_CHOICES = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
    ]
    meal_types = models.CharField(max_length=100, choices=MEAL_CHOICES)
    meal_count = models.IntegerField()

class DonationTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_request =models.ForeignKey(FoodRequest,on_delete=models.CASCADE)
    available_food_count = models.IntegerField()
    pickup_time = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(null=True,blank=True)
    


class DonationConfirmationTicket(models.Model):
    donation_ticket = models.OneToOneField(DonationTicket, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    received_quantity = models.IntegerField(null=True, blank=True)
    response_message = models.TextField(null=True, blank=True)         
                

    
