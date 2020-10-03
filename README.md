Assumptions:

- /shorten is only to be used for POST (i.e. not for other request methods)
- The text next to error codes is the 'reason_phrase' (and not e.g. part of the body or else)
- Even if some of the response body content looks like json I assume it only looks like json but in fact it is text.


Possible improvement:
- Make a ShortcodeManager class to collect all shortcode utils functions in one place.
- Use other logic to produce unique shortcode when already many shortcodes are taken (random.sample() gets slower the less available combinations...)