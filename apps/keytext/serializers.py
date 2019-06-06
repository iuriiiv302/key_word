from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.keytext.models import KeyWord


class TextkeySerializer(serializers.ModelSerializer):
    key = serializers.CharField()

    def validate_key_search(self, object):
        key = KeyWord.objects.filter(key=object)
        if not key:
            raise ValidationError("Not key")
        return object

    class Meta:
        model = KeyWord
        fields = ('key',)


class TextkeyAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = '__all__'
