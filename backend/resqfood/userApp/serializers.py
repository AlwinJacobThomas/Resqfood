from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','password','is_organization','is_individual']

class UserRegistrationSerializer(serializers.ModelSerializer):
    is_organization = serializers.BooleanField(write_only=False)
    is_individual = serializers.BooleanField(write_only=False)
    
    
    class Meta:
        model = User        
        fields = ('id','username','email','password','is_organization','is_individual')
        extra_kwargs = {'password':{'write_only': True}}
        
    def create(self, validated_data):
        is_organization = validated_data.pop('is_organization', False)
        is_individual = validated_data.pop('is_individual', False)
        user = User.objects.create_user(**validated_data)
        user.is_organization = is_organization
        user.is_individual = is_individual
        user.save()
        
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)