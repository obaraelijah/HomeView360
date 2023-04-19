import logging 

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,generics,permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import PropertyNotFound
from .models import Property,PropertyViews
from .pagination import PropertyPagination
from .serializers import (
    PropertyCreateSerializer,
    PropertySerializer,
    PropertyViewSerializer
)

logger = logging.getLogger(__name__)


class PropertyFilter(django_filters.FilterSet):

    advert_type = django_filters.CharFilter(
        field_name="advert_type", lookup_expr="iexact"
    )

    property_type = django_filters.CharFilter(
        field_name="property_type", lookup_expr="iexact"
    )

    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Property
        fields = ["advert_type", "property_type", "price"]

