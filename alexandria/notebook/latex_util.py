import requests

from urllib.parse import urljoin


class LaTeXUtil:
    def __init__(self, base_uri):
        self.base_uri = base_uri

    def svg_uri(self, tex):
        url = urljoin(self.base_uri, "2svg")
        session = requests.Session()
        session.headers['content-type'] = 'text/plain'
        response = session.post(url, data=tex)
        return response.headers['location']
