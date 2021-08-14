from django.contrib.auth.models import User


from rest_framework import viewsets, status, pagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from short_url.models import Url
from short_url.serializers import UrlSerializer


class UrlsViewSet(viewsets.ModelViewSet):
    '''API endpoint that allows Request Tests to be viewed or edited.'''
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
