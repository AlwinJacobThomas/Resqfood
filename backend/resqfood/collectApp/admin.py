from django.contrib import admin
from .models import DonationConfirmationTicket,DonationTicket,FoodRequest,IndividualProfile,Location,OrganizationProfile
# Register your models here.
admin.site.register(DonationConfirmationTicket)
admin.site.register(DonationTicket)
admin.site.register(FoodRequest)
admin.site.register(IndividualProfile)
admin.site.register(OrganizationProfile)
admin.site.register(Location)