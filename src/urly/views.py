import requests
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import ShortcodeForm
from .utils import make_unique_shortcode, url_exists, is_invalid
from .models import Shortcode


def homepage(request):
    """View for '/', i.e. homepage.""" 
    form = ShortcodeForm()
    return render(request, 'urly/index.html', {'form':form})


def get_shortcode(request):
    """View to shorten url."""
    form = ShortcodeForm(data=request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        shortcode = cd['shortcode']
        entry = form.save(commit=False)
        if url_exists(cd['url']) != True:
            response = HttpResponse('Url not present.<br><a href="/">Try again</a>.')
            response.status_code = 400
            response.reason_phrase = 'Url not present'
            return response
        elif is_invalid(shortcode):
            response = HttpResponse('The provided shortcode is invalid.<br>\
                    <a href="/">Try again</a>.')
            response.status_code = 412
            response.reason_phrase = 'The provided shortcode is invalid'
            return response
        shortcodes = [getattr(c, 'shortcode') for c in Shortcode.objects.all()]
        if shortcode in shortcodes:
            response = HttpResponse('Shortcode already in use.<br>\
                <a href="/">Try again</a>.')
            response.status_code = 409
            response.reason_phrase = 'Shortcode already in use'
            return response
        elif shortcode == '':
            entry.shortcode = make_unique_shortcode(6, shortcodes)
        entry.redirectCount = 0
        entry.save()
        response = HttpResponse('{"shortcode":"%s"}' % (entry.shortcode))
        response.status_code = 201
        return response
    return render(request, 'urly/index.html', {'form':form})


def check_shortcode(request, shortcode_2):
    """View to check whether shortcode is already in db."""
    try:
        shortcode = Shortcode.objects.get(shortcode=shortcode_2)
    except:
        response = HttpResponse('Shortcode not found.<br><a href="/">Try again</a>.')
        response.status_code = 404
        response.reason_phrase = 'Shortcode not found'
        return response
    else:
        response = HttpResponseRedirect(shortcode.url)
        response.status_code = 302
        response['Location'] = shortcode.url
        shortcode.lastRedirect = datetime.today()
        shortcode.redirectCount = shortcode.redirectCount + 1
        shortcode.save()
        return response
        

def get_stats(request, shortcode):
    """View to get shortcode statistics."""
    try:
        shortcode = Shortcode.objects.get(shortcode=shortcode)
    except:
        response = HttpResponse('Shortcode not found.<br><a href="/">Try again</a>.')
        response.status_code = 404
        response.reason_phrase = 'Shortcode not found'
        return response
    else:
        response = HttpResponse('{"created": "%s", "lastRedirect": "%s", "redirectCount": %s}'\
             % (shortcode.created, shortcode.lastRedirect, shortcode.redirectCount))
        response.status_code = 200
        return response