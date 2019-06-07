from django.http import JsonResponse
from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.keytext.models import KeyWord
from apps.keytext.serializers import TextkeyAllSerializer, TextkeySerializer


class TextFilterKey(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = ()
    serializer_class = TextkeySerializer

    @serialize_decorator(TextkeySerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data
        text = KeyWord.objects.filter(key=validated_data['key'])
        response_data = TextkeyAllSerializer(text, many=True).data
        print(response_data)
        if response_data == []:
            return JsonResponse({'key': 'incorrect'})
        return Response(response_data)

    def get(self, request):
        text = KeyWord.objects.order_by('key')
        return Response(TextkeyAllSerializer(text, many=True).data)
