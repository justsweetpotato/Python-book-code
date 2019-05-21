from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions

from .models import Sprint
from .serializers import SprintSerializer


class SprintViewSet(viewsets.ModelViewSet):
    '''API endpoint for listing and creating sprints.'''

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer


class DefaultsMixin(object):
    '''Default settings for view authentication, permissions, filtering and pagination.'''

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    '''API endpoint for listing and creating sprints.'''

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
