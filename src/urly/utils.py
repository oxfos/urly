import requests
import string, random
from .models import Shortcode


def make_shortcode(l):
    """Function to create random shortcode of length l."""
    alphanum = string.ascii_lowercase + string.digits + '_'
    code = ''
    for i in range(l):
        code = code + random.sample(alphanum, 1)[0]
    return code


def make_unique_shortcode(l):
    """Function to create unique get_shortcode."""
    shortcodes = Shortcode.objects.all()
    shortcode = make_shortcode(l)
    while shortcode in shortcodes:
        shortcode = make_shortcode(l)
    return shortcode


def is_not_unique(shortcode):
    """Test if shortcode is unique."""
    return Shortcode.objects.filter(shortcode=shortcode).exists()


def url_exists(url):
    """Function to test whether url exists."""
    try:
        response = requests.get(url)
    except:
        return False
    else:
        return False if response.status_code != 200 else True


def is_invalid(shortcode):
    """Function to test whether provided shortcode is valid."""
    alphanum = string.ascii_lowercase + string.digits + '_'
    return 0 in [c in alphanum for c in shortcode]

