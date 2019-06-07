from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.keytext.models import KeyWord


class TextkeySerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = ('key',)


class TextkeyAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = '__all__'
