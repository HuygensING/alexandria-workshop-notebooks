from IPython.display import Latex

from alexandria_markup.client.alexandria_markup import AlexandriaMarkup

class DocumentProxy:
    def __init__(self, uuid: str, alexandria: AlexandriaMarkup):
        self.uuid = uuid
        self.documents = alexandria.documents

    def __dir__(self):
        return ['uuid', 'set_lmnl', 'get_lmnl', 'show_text_markup', 'show_matrix', 'show_kdtree', 'show_markupdepth']

    def set_lmnl(self, lmnl):
        self.documents.set(self.uuid, lmnl)

    def get_lmnl(self):
        return self.documents.lmnl(self.uuid)

    def show_text_markup(self):
        latex = self.documents.document_latex(self.uuid)
        Latex(latex)

    def show_matrix(self):
        latex = self.documents.matrix_latex(self.uuid)
        Latex(latex)

    def show_kdtree(self):
        latex = self.documents.kdtree_latex(self.uuid)
        Latex(latex)

    def show_markupdepth(self):
        latex = self.documents.markupdepth_latex(self.uuid)
        Latex(latex)

    def __str__(self):
        return "DocumentProxy::" + self.uuid


class AlexandriaError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
