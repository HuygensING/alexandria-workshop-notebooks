"""
   Copyright 2017 Huygens ING

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

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
