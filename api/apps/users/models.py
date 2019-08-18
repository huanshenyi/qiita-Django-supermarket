from datetime import datetime

from django.db import models
# AbstractUserモデルを上書きする
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    """
    ユーザー
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="名前")
    birthday = models.DateField(null=True, blank=True, verbose_name="生年月日")
    mobile = models.CharField(max_length=20, verbose_name="携帯番号")
    gender = models.CharField(max_length=6, choices=(("male", "男性"), ("female", "女性"), ("secret", "非公開")),
                              default="male", verbose_name="性別")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="アドレス")

    class Meta:
        verbose_name = "ユーザー"
        verbose_name_plural = verbose_name

    def __str__(self):
       return self.username


class VerifyCode(models.Model):
    """
    メール認証コード
    """
    code = models.CharField(max_length=10, verbose_name="メール検証コード")
    mobile = models.CharField(max_length=11, verbose_name="携帯番号")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "メール認証コード"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


