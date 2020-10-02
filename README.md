Assumptions:

- /shorten is only to be used for POST (i.e. not for other request methods)
- The text next to error codes is the 'reason_phrase' (and not e.g. part of the body or else)
- Even if some of the response body content looks like json I assume it only looks like json and in fact it is text.