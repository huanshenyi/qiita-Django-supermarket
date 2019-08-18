from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

from goods.models import Goods

# Create your models here.
User = get_user_model()


class UserFav(models.Model):
    """
    ユーザーお気に入り
    """
    user = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="商品", help_text="商品id", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "ユーザーお気に入り"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    """
    ユーザーコメント
    """
    MESSAGE_CHOICES = (
        (1, "一般メッセージ"),
        (2, "苦情"),
        (3, "質問"),
        (4, "保障問い合わせ"),
        (5, "追加注文関連"),
    )
    user = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    msg_type = models.IntegerField(choices=MESSAGE_CHOICES, default=1,
                                   verbose_name="メッセージタイプ",
                                   help_text="メッセージタイプ:1(一般メッセージ),2(苦情),3(質問),4(保障問い合わせ),5(追加注文関連)")
    subject = models.CharField(max_length=100, default="", verbose_name="テーマ")
    message = models.TextField(default="", verbose_name="メッセージ内容", help_text="メッセージ内容")
    file = models.FileField(upload_to="message/images/", verbose_name="アップロードファイル", help_text="アップロードファイル")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "ユーザーメッセージ"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    """
    ユーザーお届け先
    """
    user = models.ForeignKey(User, verbose_name="ユーザー", on_delete=models.CASCADE)
    district = models.CharField(max_length=100, default="", null=True, blank=True,  verbose_name="地域")
    province = models.CharField(max_length=100, default="", null=True, blank=True, verbose_name="県")
    city = models.CharField(max_length=100, default="", verbose_name="city")
    address = models.CharField(max_length=100, default="", verbose_name="お届け先住所")
    signer_name = models.CharField(max_length=100, default="", verbose_name="受取人名前")
    signer_mobile = models.CharField(max_length=20, default="", verbose_name="受取人番号")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "ユーザーお届け先"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
