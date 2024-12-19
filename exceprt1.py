from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.docutils import SphinxDirective
import datetime
from link import *

class ExcerptDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'date': directives.unchanged,
    }

    def run(self):
        
        content = '\n'.join(self.content)
        content_for_datetime=datetime_pattern.sub(datetime_replace_match,content)

        
        raw_html = f"""
        <ac:structured-macro ac:name="excerpt">
        <ac:parameter ac:name="nopanel">true</ac:parameter>
        <ac:rich-text-body>
           {content_for_datetime}
        </ac:rich-text-body>
        </ac:structured-macro>
        """

        return [nodes.raw('', raw_html, format='html')]

def setup(app):
    app.add_directive("except1", ExcerptDirective)
    return {'version': '1.0', 'parallel_read_safe': True}