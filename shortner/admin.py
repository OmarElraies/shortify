from django.contrib import admin
from .models import UrlData
# Register your models here.


class UrlDataAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')

admin.site.register(UrlData, UrlDataAdmin)
