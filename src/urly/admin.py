from django.contrib import admin
from .models import Shortcode


@admin.register(Shortcode)
class ShortcodeAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('url', 'shortcode', 'created')
    fields = ('url', 'shortcode', 'created')