from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile
import re

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user + creating the profile
    """
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(required=True)
    job_title = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'phone', 'job_title']

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        job_title = validated_data.pop('job_title', '')


        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        
        Profile.objects.create(
            user=user,
            phone=phone,
            job_title=job_title
        )

        return user


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing or editing the profile
    """
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'phone', 'job_title', 'role']


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for changing password with strength and length validation
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        
        if len(value) < 8:
            raise serializers.ValidationError("New password must be at least 8 characters long.")


        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")

        
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")

        
        if not re.search(r'\d', value):
            raise serializers.ValidationError("Password must contain at least one number.")

        
        if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', value):
            raise serializers.ValidationError("Password must contain at least one special character.")

        return value
   
    def validate(self, data):
        user = self.context['request'].user

        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({"old_password": "Wrong password."})

        if data['old_password'] == data['new_password']:
            raise serializers.ValidationError({"new_password": "New password cannot be the same as the old password."})

        return data