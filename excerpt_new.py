

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged
from link import *

class ExpandDirective(Directive):
    
    has_content = True
    
    def run(self):
       
        
        content = self._parse_nested_content()
       
        
        content = datetime_pattern.sub(datetime_replace_match,content)
        content=status_pattern.sub(status_replace_match,content)

        raw_html = f"""
           <ac:structured-macro ac:name="excerpt" >
            
            <ac:rich-text-body>
              {content}
            </ac:rich-text-body>
           
            </ac:structured-macro>

                """
        raw_node = nodes.raw('', raw_html, format='html')
        return [raw_node]

    def _parse_nested_content(self):
        '''This function works for nested macros'''
        #env = self.state.document.settings.env
        node = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, node)
        return ''.join(node.astext())


def setup(app):
    
    app.add_directive('excerpt_n', ExpandDirective)
