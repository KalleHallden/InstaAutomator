# flake8: noqa
# pylint: disable=unused-import
try:
    import urllib.request as compat_urllib_request
except ImportError:  # Python 2
    import urllib2 as compat_urllib_request

try:
    import urllib.error as compat_urllib_error
except ImportError:  # Python 2
    import urllib2 as compat_urllib_error

try:
    import urllib.parse as compat_urllib_parse
except ImportError:  # Python 2
    import urllib as compat_urllib_parse

try:
    from urllib.parse import urlparse as compat_urllib_parse_urlparse
except ImportError:  # Python 2
    from urlparse import urlparse as compat_urllib_parse_urlparse

try:
    import urllib.parse as compat_urlparse
except ImportError:  # Python 2
    import urlparse as compat_urlparse

try:
    import http.client as compat_http_client
except ImportError:  # Python 2
    import httplib as compat_http_client

try:
    from urllib.request import urlretrieve as compat_urlretrieve
except ImportError:  # Python 2
    from urllib import urlretrieve as compat_urlretrieve
