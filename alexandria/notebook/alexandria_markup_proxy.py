from alexandria_markup.client.alexandria_markup import *
from alexandria.notebook.latex_util import LaTeXUtil
from alexandria.notebook.document_proxy import DocumentProxy


class AlexandriaMarkupProxy:
    def __init__(self, server_url, latex_server_url):
        self.alexandria = AlexandriaMarkup(server_url)
        self.latexutil = LaTeXUtil(latex_server_url)

    def __dir__(self):
        return ['add_document']

    def add_document(self, path):
        with open(path, 'r') as f:
            lmnl = f.read()
        uuid = self.alexandria.documents.add(lmnl).uuid
        return DocumentProxy(uuid, self.alexandria, self.latexutil)
