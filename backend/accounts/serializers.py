from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'full_name', 'phone', 'job_title', 'role', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
    def get_full_name(self, obj):
        return obj.user.get_full_name() or obj.user.username
