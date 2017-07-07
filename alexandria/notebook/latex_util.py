import requests

from urllib.parse import urljoin


class LaTeXUtil:
    def __init__(self, base_uri):
        self.base_uri = base_uri

    def svg_uri(self, tex):
        url = urljoin(self.base_uri, "2svg")
        session = requests.Session()
        session.headers['content-type'] = 'text/plain; charset=UTF-8'
        response = session.post(url, data=tex.encode('utf-8'))
        if 'location' in response.headers:
            svg_uri = response.headers['location']
            return svg_uri
        else:
            raise ValueError('tex-util-server returned an error: ', response.json())