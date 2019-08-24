import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    goodsのfilter
    """
    price_min = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte', help_text="最小額")
    price_max = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte', help_text="最大額")

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
