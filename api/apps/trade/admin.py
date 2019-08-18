from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ["user", "goods", "goods_num", ]


class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ["user", "order_sn",  "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]

    class OrderGoodsInline(InlineModelAdmin):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline]


admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(OrderInfo, OrderInfoAdmin)

