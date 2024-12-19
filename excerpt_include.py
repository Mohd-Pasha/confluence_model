from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.docutils import SphinxDirective
import datetime

class ExcerptDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    option_spec = {
        'title': directives.unchanged,
    }

    def run(self):
        title = self.options.get('title', '')
        
        
        raw_html = f"""
       <ac:structured-macro ac:name="excerpt-include" >
        <ac:parameter ac:name="">
           <ac:link>
           <ri:page ri:content-title="{title}"/>
           </ac:link>
         </ac:parameter>
         <ac:parameter ac:name="nopanel">true</ac:parameter>
      </ac:structured-macro>
        """

        return [nodes.raw('', raw_html, format='html')]

def setup(app):
    app.add_directive("excerpt_include", ExcerptDirective)
    return {'version': '1.0', 'parallel_read_safe': True}
