from django.core.management import call_command
from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


@api_view()
@permission_classes([AllowAny])
def reset(request):
    if settings.DEBUG:
        call_command("reset_db", interactive=False)
        call_command("migrate")
        call_command("setupe2e")

    return Response(status=status.HTTP_200_OK)
