from rest_framework import serializers
from .models import Upload
from .models import Summary

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'