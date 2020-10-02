
import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import ShortcodeForm
from .utils import get_unique_shortcode, url_exists, is_not_unique, is_invalid
from .models import Shortcode


def homepage(request):
    """View for / url, i.e. homepage.""" 
    form = ShortcodeForm()
    return render(request, 'urly/index.html', {'form':form})


def get_shortcode(request):
    """View to shorten url."""
    form = ShortcodeForm(data=request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        entry = form.save(commit=False)
        if url_exists(cd['url']) != True:
            response = HttpResponse('Url not present.<br><a href="/">Try again</a>.')
            response.reason_phrase = 'Url not present'
            response.status_code = 400
            return response
        elif is_not_unique(cd['shortcode']):
            response = HttpResponse('Shortcode already in use.<br><a href="/">Try again</a>.')
            response.reason_phrase = 'Shortcode already in use'
            response.status_code = 409
            return response
        elif is_invalid(cd['shortcode']):
            response = HttpResponse('The provided shortcode is invalid.<br><a href="/">Try again</a>.')
            response.reason_phrase = 'The provided shortcode is invalid'
            response.status_code = 412
            return response
        elif cd['shortcode'] == '':
            entry.shortcode = get_unique_shortcode(6)
        entry.save()
        response = HttpResponse('{"shortcode":"%s"}' % (entry.shortcode))
        response.status_code = 201
        return response
    return render(request, 'urly/index.html', {'form':form})


def check_shortcode(request, shortcode_2):
    """View to check whether shortcode in db."""
    try:
        shortcode = Shortcode.objects.get(shortcode=shortcode_2)
    except:
        response = HttpResponse('Shortcode not found')
        response.status_code = 404
        response.reason_phrase = 'Shortcode not found'
        return response
    else:
        response = HttpResponseRedirect(shortcode.url)
        response.status_code = 302
        response['Location'] = shortcode.url
        return response
        
