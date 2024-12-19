from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.docutils import SphinxDirective
import datetime

class ExcerptDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'date': directives.unchanged,
    }

    def run(self):
        date = self.options.get('date', '')
        comment = '\n'.join(self.content)

        
        raw_html = f"""
        <ac:structured-macro ac:name="excerpt">
        <ac:parameter ac:name="nopanel">true</ac:parameter>
        <ac:rich-text-body>
        <p>
        {comment}
        <time datetime="{date}" />
        <ac:structured-macro ac:name="status">
        <ac:parameter ac:name="title">Completed</ac:parameter>
        <ac:parameter ac:name="colour">Green</ac:parameter>
        </ac:structured-macro>
        </p>
        </ac:rich-text-body>
        </ac:structured-macro>
        """

        return [nodes.raw('', raw_html, format='html')]

def setup(app):
    app.add_directive("except", ExcerptDirective)
    return {'version': '1.0', 'parallel_read_safe': True}
