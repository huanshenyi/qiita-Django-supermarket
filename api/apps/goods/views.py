from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods
from .models import GoodsCategory
from .serializer import GoodsSerializer
from .serializer import CategorySerializer
from .filters import GoodsFilter


class GoodsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
     queryset = Goods.objects.all()
     serializer_class = GoodsSerializer
     pagination_class = GoodsSetPagination
     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
     filterset_class  = GoodsFilter
     search_fields = ['name', 'goods_brief']
     ordering_fields = ['shop_price']


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer