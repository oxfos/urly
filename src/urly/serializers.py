from rest_framework import serializers
from .models import Shortcode


class ShortcodeSerializer(serializers.ModelSerializer):
    """Shortcode model serializer for make_shortcode view."""

    class Meta:
        model = Shortcode
        fields = ['shortcode']


class ShortcodeStatsSerializer(serializers.ModelSerializer):
    """Shortcode model serializer for for get_stats view."""

    class Meta:
        model = Shortcode
        fields = ['created', 'lastRedirect', 'redirectCount']

