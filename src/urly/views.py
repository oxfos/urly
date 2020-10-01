
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import ShortcodeForm
from .utils import get_unique_shortcode, url_exists, is_not_unique
from .models import Shortcode


def homepage(request):
    """View for / url, i.e. homepage.""" 
    form = ShortcodeForm()
    return render(request, 'urly/index.html', {'form':form})


def shorten(request):
    """View to shorten url."""
    if request.method == 'POST':
        form = ShortcodeForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            entry = form.save(commit=False)
            if url_exists(cd['url']) != True:
                return redirect('urly:error_400')
            if is_not_unique(cd['shortcode']):
                return redirect('urly:error_409')
            if cd['shortcode'] == '':
                entry.shortcode = get_unique_shortcode(6)
            entry.save()
    return render(request, 'urly/index.html', {'form':form})


# ERROR VIEWS

def error_400(request, exception=None):
    response = render(request, 'urly/errors/400.html')
    response.reason_phrase = 'Url not present'
    response.status_code = 400
    return response


def error_404(request, exception=None):
    response = render(request, 'urly/errors/404.html')
    response.reason_phrase = 'Shortcode not found'
    response.status_code = 404
    return response


def error_409(request, exception=None):
    response = render(request, 'urly/errors/409.html')
    response.reason_phrase = 'Shortcode already in use'
    response.status_code = 409
    return response


def error_412(request, exception=None):
    response = render(request, 'urly/errors/412.html')
    response.reason_phrase = 'The provided shortcode is invalid'
    response.status_code = 412
    return response