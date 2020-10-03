"""
- make 10000 shortcodes with the provided function
- check that they don't contain certain characters and are long l
"""

import itertools, string
from django.test import TestCase
from urly.utils import *


class Make_shortcode_test(TestCase):
    """Test class for make_shortcode function."""

    @classmethod
    def setUpTestData(self):
        # Prepare shortcode set.
        self.codes = []
        for i in range(1000):
            self.codes.append(make_shortcode(6))
        self.jcodes = ''.join(self.codes)

    def test_shortcode(self):
        self.assertTrue(len(c)==6 for c in self.codes)
        self.assertTrue(0 in [c in self.jcodes for c in ['%', '$', '#', '@']])


class Make_unique_shortcode_test(TestCase):
    """Test class for make_unique_shortcode function."""

    @classmethod
    def setUpTestData(self):
        #prepare test set (it is convoluted because originally I wanted to have more repeats...)
        combinations = [c for c in itertools.product(alphanum, repeat=1)]
        make_strings = lambda tu : ''.join(list(''.join(v) for v in tu))
        self.string_combinations = [make_strings(c) for c in combinations]

    
    def test_make_unique_shortcode(self):
        # Test shortcode is unique.
        newset = [e[0] for e in self.string_combinations]
        newset.remove('d')
        unique = make_unique_shortcode(1, newset)
        self.assertEqual(unique, 'd')
