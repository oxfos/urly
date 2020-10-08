from rest_framework import serializers
from ..models import Shortcode


class ShortcodeStatsSerializer(serializers.ModelSerializer):
    """Serializer for a model object."""

    class Meta:
        model = Shortcode
        fields = ['created', 'lastRedirect', 'redirectCount']

