from datetime import datetime

from django.db import models


class GoodsCategory(models.Model):
    """
    商品カテゴリー
    """
    CATEGORY_TYPE = (
        (1, "一級カテゴリー"),
        (2, "二級カテゴリー"),
        (3, "三級カテゴリー")
    )

    name = models.CharField(default="", max_length=50, verbose_name="カテゴリー名", help_text="カテゴリー名")
    code = models.CharField(default="", max_length=30, verbose_name="カテゴリーコード", help_text="カテゴリーコード")
    desc = models.TextField(default="", verbose_name="カテゴリー説明", help_text="カテゴリー説明")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="カテゴリーレベル", help_text="カテゴリーレベル")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="親カテゴリー", help_text="親カテゴリー",
                                        on_delete=models.CASCADE, related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="ナビなのか", help_text="ナビなのか")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "商品カテゴリー"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    ブランド名
    """
    category = models.ForeignKey(GoodsCategory, related_name="brands", null=True, blank=True,
                                 verbose_name="商品カテゴリー名", on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=30, verbose_name="ブランド名", help_text="ブランド名")
    desc = models.CharField(default="", max_length=200, verbose_name="ブランド説明", help_text="ブランド説明")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "ブランド"
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand"

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, null=True, blank=True,
                                 verbose_name="商品カテゴリー", on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品識別番号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    click_num = models.IntegerField(default=0, verbose_name="クリック数")
    sold_num = models.IntegerField(default=0, verbose_name="販売数")
    fav_num = models.IntegerField(default=0, verbose_name="お気に入り登録数")
    goods_num = models.IntegerField(default=0, verbose_name="在庫数")
    market_price = models.FloatField(default=0, verbose_name="原価")
    shop_price = models.FloatField(default=0, verbose_name="販売値段")
    goods_brief = models.TextField(max_length=500, verbose_name="商品説明")
    ship_free = models.BooleanField(default=True, verbose_name="送料負担")
    goods_front_image = models.ImageField(max_length=200, upload_to="goods/images/",
                                          null=True, blank=True, verbose_name="表紙")
    is_new = models.BooleanField(default=False, verbose_name="新品なのか")
    is_hot = models.BooleanField(default=False, verbose_name="売れているのか")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品swiperImages
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", verbose_name="画像", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "商品swiperImages"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    swiper用の商品image
    """
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="banner", verbose_name="ホームページswiper用画像")
    index = models.IntegerField(default=0, verbose_name="swiper順番")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "swiper用の商品image"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, related_name="category",
                                 verbose_name="商品カテゴリー", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, related_name='goods', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "ホームページ商品カテゴリー広告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    人気キーワード
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="人気キーワード")
    index = models.IntegerField(default=0, verbose_name="並び順")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="挿入時間")

    class Meta:
        verbose_name = "人気キーワード"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords