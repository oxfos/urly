from django.test import TestCase
from urly.models import Shortcode



class Test_homepage_view(TestCase):
    """Test class for homepage view."""

    def test_get_page(self):
        # Test GET works as expected.
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'urly/index.html') 


class Test_makeshortcode_view(TestCase):
    """Test class for make_shortcode view."""

    def setUp(self):
        Shortcode.objects.create(url='https://www.google.com', shortcode='catch_',\
            redirectCount=0)

    def test_inexistent_url(self):
        # Test valid but non-existent url.
        response = self.client.post('/shorten', {'url':'http://www.79as.com/'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.reason_phrase, 'Url not present')

    def test_shortcode_is_not_unique(self):
        # Test shortcode already in use.
        response = self.client.post('/shorten', {'url':'https://www.google.com', 'shortcode': 'catch_'})
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.reason_phrase, 'Shortcode already in use')

    def test_shortcode_is_invalid(self):
        # Test invalid shortcode.
        response = self.client.post('/shorten', {'url':'https://www.google.com', 'shortcode':'catch$'})
        self.assertEqual(response.status_code, 412)
        self.assertEqual(response.reason_phrase, 'The provided shortcode is invalid')

    def test_existent_url(self):
        # Test valid and existent url.
        response = self.client.post('/shorten', {'url': 'https://www.google.com'})
        self.assertEqual(response.status_code, 201)
        self.assertContains(response, 'shortcode', status_code=201)
        self.assertNotIn('url', str(response.content))



class Test_check_shortcode_view(TestCase):
    """Test class for check_shortcode view."""

    def setUp(self):
        # Create a db Shortcode object.
        self.entry = Shortcode.objects.create(url="https://www.google.com", shortcode="catch_",\
            redirectCount=0)

    def test_shortcode_exists(self):
        # Tests an existing shortcode...
        response = self.client.get('/catch_')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.entry.url, fetch_redirect_response=False)
        self.assertEqual(response['Location'], self.entry.url)

    def test_shortcode_does_not_exist(self):
        # Tests an inexistent shortcode...
        response = self.client.get('/catch1')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.reason_phrase, 'Shortcode not found')