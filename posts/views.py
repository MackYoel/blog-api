import django_filters

from rest_framework import filters, permissions, viewsets

from utils import pagination

from . import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.PostSerializer
    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    ordering = ('-pk',)
    ordering_fields = ('pk',)
    filter_fields = {
        'slug': ['icontains'],
    }
    queryset = models.Post.objects.filter(is_active=True)
