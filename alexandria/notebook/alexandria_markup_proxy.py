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

from alexandria_markup.client.alexandria_markup import *
from alexandria.notebook.latex_util import LaTeXUtil
from alexandria.notebook.document_proxy import DocumentProxy


class AlexandriaMarkupProxy:
    def __init__(self, server_url, latex_server_url):
        self.alexandria = AlexandriaMarkup(server_url)
        self.latexutil = LaTeXUtil(latex_server_url)

    def __dir__(self):
        return ['add_document_from_lmnl_file', 'add_document_from_texmecs_file',
                'add_document_from_lmnl_text', 'add_document_from_texmecs_text']

    def add_document_from_lmnl_file(self, path):
        with open(path, mode='r', encoding='utf-8') as f:
            lmnl = f.read()
        return self.add_document_from_lmnl_text(lmnl)

    def add_document_from_texmecs_file(self, path):
        with open(path, mode='r', encoding='utf-8') as f:
            texmecs = f.read()
        return self.add_document_from_texmecs_text(texmecs)

    def add_document_from_lmnl_text(self, lmnl):
        uuid = self.alexandria.documents.add_from_lmnl(lmnl).uuid
        return DocumentProxy(uuid, self.alexandria, self.latexutil)

    def add_document_from_texmecs_text(self, texmecs):
        uuid = self.alexandria.documents.add_from_texmecs(texmecs).uuid
        return DocumentProxy(uuid, self.alexandria, self.latexutil)
