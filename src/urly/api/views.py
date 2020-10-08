from django.http import JsonResponse, HttpResponse
from ..models import Shortcode
from .serializers import ShortcodeStatsSerializer




def api_shortcode_stats(request, shortcode):
    """Function view returning shortcode stats."""
    try:
        shortcode = Shortcode.objects.get(shortcode=shortcode)
    except:
        response = HttpResponse('Shortcode not found.<br><a href="/">Try again</a>.')
        response.status_code = 404
        response.reason_phrase = 'Shortcode not found'
        return response
    else:
        serializer = ShortcodeStatsSerializer(shortcode, many=False)
        return JsonResponse(serializer.data, status=200)