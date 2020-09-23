from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SiteSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()


class UpdateUserActiveStatusSerializer(serializers.ModelSerializer):
    """
    Serializer for active status change endpoint.
    """

    class Meta:
        model = User
        fields = ('id', 'is_active')
