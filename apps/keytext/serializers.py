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


class TextAllSerializer(serializers.ModelSerializer):
    key = serializers.ModelSerializer

    def validate_key(self, attrs):
        key = KeyWord.objects.filter(key=attrs).first()
        if not key:
            return attrs
        else:
            raise ValidationError("the key is repeated, it must be unique.")

    class Meta:
        model = KeyWord
        fields = ('key', 'full_text')


class TextUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    def validate_id(self, value):
        text = KeyWord.objects.filter(id=value).first()
        if not text:
            raise ValidationError("there is no text with such id")
        return value

    class Meta:
        model = KeyWord
        fields = ['id', 'key', 'full_text']
