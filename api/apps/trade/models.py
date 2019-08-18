from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods
from datetime import datetime

User = get_user_model()


class ShoppingCart(models.Model):
    """
    ショッピングカート
    """
    user = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name="購入数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "ショッピングカート"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.goods_num)


class OrderInfo(models.Model):
    """
    注文()
    """
    ORDER_STATUS = (
        ("success", "成功"),
        ("TRADE_CLOSED", "時間オーバー"),
        ("WAIT_BUYER_PAY", "クリエイトオーダー"),
        ("cancel", "キャンセル"),
        ("cancel", "支払い待ち")
    )

    user = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    order_sn = models.CharField(max_length=40, null=True, blank=True, unique=True, verbose_name="注文番号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="オーダー番号")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="注文状態")
    post_script = models.CharField(max_length=200, verbose_name="注文コメント")
    order_mount = models.FloatField(default=0.0, verbose_name="注文金額")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支払い時間")
    address = models.CharField(max_length=100, default="", verbose_name="届出先")
    signer_name = models.CharField(max_length=20, default="", verbose_name="受取人")
    singer_mobile = models.CharField(max_length=20, verbose_name="連絡先")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "注文"
        verbose_name_plural = verbose_name

    def __str__(self):
       return str(self.order_sn)


class OrderGoods(models.Model):
    """
    注文の商品詳細
    """
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="注文詳細", related_name="goods")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    goods_num = models.IntegerField(default=0, verbose_name="商品数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "注文の商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)


