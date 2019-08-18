from django.contrib import admin
from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(admin.ModelAdmin):
    list_display = ['user', 'goods', "add_time"]


class UserLeavingMessageAdmin(admin.ModelAdmin):
    list_display = ['user', "subject", "message", "file", "add_time"]


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user', "district", "address", "signer_name", "signer_mobile", "add_time"]


admin.site.register(UserFav, UserFavAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
