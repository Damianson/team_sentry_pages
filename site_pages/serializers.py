from rest_framework import serializers
from site_pages.models import AddPage

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddPage
        fields = '__all__'

class PageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddPage
        fields = ['content']