from rest_framework import serializers
from ..models import Shortcode


class ShortcodeSerializer(serializers.ModelSerializer):
    """Serializer for a model object."""

    class Meta:
        model = Shortcode
        fields = ['shortcode', 'url']