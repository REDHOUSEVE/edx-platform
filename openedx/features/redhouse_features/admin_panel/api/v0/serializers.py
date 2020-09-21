from rest_framework import serializers


class SiteSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
