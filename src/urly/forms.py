from django import forms
from .models import Shortcode


class ShortcodeForm(forms.ModelForm):
    """ModelForm to handle Shortcode data."""
    class Meta:
        model = Shortcode
        fields = ['url', 'shortcode']

