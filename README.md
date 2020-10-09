# Urly


Webservice that shortens urls.

Created with Python (3.6.9) package Django.<br>
Serialization with [django rest framework](https://www.django-rest-framework.org/).<br>
Custom status codes and reason phrases.


## Use

1. Make short code

`https://urly-main.herokuapp.com/`

- Insert url
- Insert short code (optional)

2. Acces url via shortcode

Add shortcode at the end of the url:

`https://urly-main.herokuapp.com/your-shortcode-here`

3. Check shortcode statistics

Add `your-shortcode-here/stats` in url:

`https://urly-main.herokuapp.com/your-shortcode-here/stats`