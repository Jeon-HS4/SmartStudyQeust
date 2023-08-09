from rest_framework import serializers

class PageContentSerializer(serializers.Serializer):
    url = serializers.URLField()
    content = serializers.CharField()