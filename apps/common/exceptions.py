from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotFound
from rest_framework.response import Response
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, AuthenticationFailed):
        return Response(response.data, status=status.HTTP_401_UNAUTHORIZED)

    return response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        Response({'error': str(exc)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    raise NotFound('You entered an invalid id', code=500)
