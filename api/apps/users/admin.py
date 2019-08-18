from django.contrib import admin

from .models import VerifyCode, UserProfile


# class BaseSetting(admin.ModelAdmin):
#     enable_themes = True
#     use_bootswatch = True
#
#
# class GlobalSettings(admin.ModelAdmin):
#     site_title = "ネットスーパー"
#     site_footer = "supermarket_Back"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthday', 'mobile', 'gender', 'email']


class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'mobile', "add_time"]


admin.site.register(VerifyCode, VerifyCodeAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

