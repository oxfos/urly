from django.contrib import admin
from .models import Shortcode


@admin.register(Shortcode)
class ShortcodeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'lastRedirect')
    list_display = ('url', 'shortcode', 'created', 'lastRedirect')
    fields = ('url', 'shortcode', 'created', 'lastRedirect')