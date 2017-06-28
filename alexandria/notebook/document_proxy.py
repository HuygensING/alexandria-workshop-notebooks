from IPython.display import display, SVG, HTML

from alexandria_markup.client.alexandria_markup import AlexandriaMarkup
from alexandria.notebook.latex_util import LaTeXUtil


class DocumentProxy:
    def __init__(self, uuid: str, alexandria: AlexandriaMarkup, latexutil: LaTeXUtil):
        self.uuid = uuid
        self.documents = alexandria.documents
        self.latexutil = latexutil

    def __dir__(self):
        return ['uuid', 'set_lmnl', 'get_lmnl', 'show_text_markup', 'show_matrix', 'show_kdtree', 'show_markupdepth', 'query']

    def __str__(self):
        return "DocumentProxy::" + self.uuid

    def set_lmnl(self, lmnl):
        self.documents.set(self.uuid, lmnl)

    def get_lmnl(self):
        return self.documents.lmnl(self.uuid)

    def query(self, tagql):
        return self.documents.query(self.uuid, tagql)

    def show_text_markup(self):
        latex = self.documents.document_latex(self.uuid)
        self.show_latex(latex)

    def show_matrix(self):
        latex = self.documents.matrix_latex(self.uuid)
        self.show_latex(latex)

    def show_kdtree(self):
        latex = self.documents.kdtree_latex(self.uuid)
        self.show_latex(latex)

    def show_markupdepth(self):
        latex = self.documents.markupdepth_latex(self.uuid)
        self.show_latex(latex)

    def show_latex(self, latex):
        svg_url = self.latexutil.svg_uri(latex)
        display(SVG(url=svg_url))
        display(HTML('<a href="' + svg_url + '" target="_new" >open in new tab</a>'))


class AlexandriaError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
