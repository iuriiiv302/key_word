from django.http import JsonResponse
from drf_util.decorators import serialize_decorator
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from apps.keytext.models import KeyWord
from apps.keytext.serializers import TextkeyAllSerializer, TextkeySerializer, TextAllSerializer, TextUpdateSerializer


class TextFilterKey(GenericAPIView):
    serializer_class = TextkeySerializer
    permission_classes = (IsAuthenticated,)

    @serialize_decorator(TextkeySerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data
        text = KeyWord.objects.filter(key=validated_data['key'], user=request.user.id)
        response_data = TextkeyAllSerializer(text, many=True).data
        if response_data == []:
            return JsonResponse({'key': 'incorrect'})
        return Response(response_data)


# Show all text_User
class TextAll(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = ()
    serializer_class = TextkeyAllSerializer

    def get(self, request):
        # text = KeyWord.objects.order_by('key')
        text = KeyWord.objects.filter(user=request.user.id)
        return Response(TextkeyAllSerializer(text, many=True).data)


# Create New Text and Key
class AddNewText(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TextAllSerializer

    @serialize_decorator(TextAllSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data
        KeyWord.objects.create(
            key=validated_data['key'],
            full_text=validated_data['full_text'],
            user=request.user,
        )
        return Response(status=201)


class DeleteText(GenericAPIView):
    serializer_class = TextkeyAllSerializer
    permission_classes = (IsAuthenticated,)

    # permission_classes = (AllowAny,)

    def delete(self, request, pk):
        text = KeyWord.objects.filter(pk=pk, user=request.user.id)
        print(text)
        if text:
            text.delete()
            return Response(status=204)
        else:
            return JsonResponse({'Id': 'error'})


# Update Text and key. From ID
class UpdateText(GenericAPIView):
    serializer_class = TextUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        try:
            serializer = TextUpdateSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                text = KeyWord.objects.get(id=data['id'], user=request.user.id)
                text.user = request.user
                text.key = data['key']
                text.full_text = data['full_text']
                text.save()
                response_data = TextkeyAllSerializer(text).data
                return Response(response_data)
            if Response.status_code == 500:
                return JsonResponse({'Error': 'status_code = 500'})
            else:
                return Response(serializer.errors, status=400)
        except:
            return JsonResponse({'Id': 'Error'})
