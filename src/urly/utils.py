import requests
import string, random
from .models import Shortcode



alphanum = string.ascii_lowercase + string.digits + '_'


def make_unique_shortcode(l, set):
    """Function to create unique make_shortcode."""
    shortcode = ''.join(random.sample(alphanum,l))
    while shortcode in set:
        shortcode = ''.join(random.sample(alphanum,l))
    return shortcode


def url_exists(url):
    """Function to test whether url exists."""
    try:
        requests.get(url, timeout=(2,2))
    except:
        return False
    else:
        return True


def is_valid(shortcode):
    """Function to test whether provided shortcode is valid."""
    return (shortcode == '' or (len(shortcode) == 6 and 0 not in [c in alphanum for c in shortcode]))

