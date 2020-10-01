from django.db import models


class Shortcode(models.Model):
    """Class representing a shortcode model."""
    scode = models.CharField(max_length=6, blank=True)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.scode