# serializers.py
from rest_framework import serializers
from .models import IndividualProfile, OrganizationProfile, Location, FoodRequest, DonationTicket, DonationConfirmationTicket

class IndividualProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualProfile
        fields = '__all__'

class OrganizationProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProfile
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class FoodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodRequest
        fields = '__all__'

class DonationTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationTicket
        fields = '__all__'

class DonationConfirmationTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationConfirmationTicket
        fields = '__all__'
