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

from IPython.display import SVG, HTML, IFrame
from IPython.core.display import display

from alexandria_markup.client.alexandria_markup import AlexandriaMarkup
from alexandria.notebook.latex_util import LaTeXUtil


class DocumentProxy:
    def __init__(self, uuid: str, alexandria: AlexandriaMarkup, latexutil: LaTeXUtil):
        self.uuid = uuid
        self.documents = alexandria.documents
        self.latexutil = latexutil

    def __dir__(self):
        return ['uuid', 'get_lmnl', 'show_text_markup', 'show_matrix', 'show_kdtree', 'show_markupdepth', 'query']

    def __str__(self):
        return "DocumentProxy::" + self.uuid

    def get_lmnl(self):
        return self.documents.lmnl(self.uuid)

    def query(self, tagql):
        return self.documents.query(self.uuid, tagql)

    def show_text_markup(self):
        latex = self.documents.document_latex(self.uuid)
        self._show_latex(latex)

    def show_matrix(self):
        latex = self.documents.matrix_latex(self.uuid)
        self._show_latex(latex)

    def show_kdtree(self):
        latex = self.documents.kdtree_latex(self.uuid)
        self._show_latex(latex)

    def show_markupdepth(self):
        latex = self.documents.markupdepth_latex(self.uuid)
        self._show_latex(latex)

    def _show_latex(self, latex):
        svg_url = self.latexutil.svg_uri(latex)
        display(IFrame(src=svg_url, width=950, height=300))
        display(HTML('<a href="' + svg_url + '" target="_new" >open in new tab</a>'))


class AlexandriaError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
