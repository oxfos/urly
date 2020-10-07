from rest_framework imprt generics
from ..models import Shortcode
from .serializers import ShortcodeSerializer


class ShortcodeDetailView(generics.RetrieveAPIView):
    queryset = Shortcode.objects.all()
    serializer_class = ShortcodeSerializer