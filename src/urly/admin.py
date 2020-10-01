from django.contrib import admin
from .models import Shortcode


@admin.register(Shortcode)
class ShortcodeAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('url', 'scode', 'created')
    fields = ('url', 'scode', 'created')