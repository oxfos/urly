import itertools, string
from django.test import TestCase
from urly.utils import *


class Test_make_shortcode(TestCase):
    """Test class for make_shortcode function."""

    @classmethod
    def setUpTestData(self):
        # Prepare shortcode set.
        self.codes = []
        for i in range(1000):
            self.codes.append(make_shortcode(6))
        self.jcodes = ''.join(self.codes)

    def test_shortcode(self):
        # All shortcodes have a length of 6.
        self.assertTrue(len(c)==6 for c in self.codes)
        # Shortcodes do not contain invalid characters
        self.assertTrue(0 in [c in self.jcodes for c in ['%', '$', '#', '@']])


class Test_make_unique_shortcode(TestCase):
    """Test class for make_unique_shortcode function."""

    @classmethod
    def setUpTestData(self):
        #prepare test set (it got complexer than needed because originally 
        # I wanted to use more repeats; but I use only one for brevity.)
        combinations = [c for c in itertools.product(alphanum, repeat=1)]
        make_strings = lambda tu : ''.join(list(''.join(v) for v in tu))
        self.string_combinations = [make_strings(c) for c in combinations]

    
    def test_make_unique_shortcode(self):
        # Test shortcode is unique.
        newset = [e[0] for e in self.string_combinations]
        newset.remove('d')
        unique = make_unique_shortcode(1, newset)
        self.assertEqual(unique, 'd')


class Test_url_exists(TestCase):
    """Test class for url_exists function."""

    def test_existing_url(self):
        response = url_exists('https://www.google.com')
        self.assertTrue(response)

    def test_inexistent_url(self):
        response = url_exists('http://www.72as.no')
        self.assertFalse(response)


class Test_is_valid(TestCase):
    """Test class for is_valid function."""

    def test_empty_shortcode(self):
        self.assertTrue(is_valid(''))
    
    def test_too_short_shortcode(self):
        self.assertFalse(is_valid('sj3'))

    def test_wrong_characters_shortcode(self):
        self.assertFalse(is_valid('sjk3@_'))

    def test_valid_shortcode(self):
        self.assertTrue(is_valid('k2l_s5'))