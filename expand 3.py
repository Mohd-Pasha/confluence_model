'''This expand macro in which user can pass nested custom directives
and can write conten.'''

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged
from link import *

class ExpandDirective(Directive):
    '''This class creates custom directive for expand which extends Directive class
    from sphinx library.
    
    Parameters
    ----------
    option_spec: str -> from Directive class
        Given arguments validate with rst arguments and 
        then we can pass arguments rst to custom directive.
    
    has_content: boolean -> from Directive class
        Directive must have some content
    '''

    has_content = True
    option_spec = {
        'title': unchanged,
    }
    def run(self):
        '''
        This function access the content and pass it to the raw_html custom format.
        Replacing some input format in link and status format.

        Parameters
        ----------

        title: str
            It access value which passed in rst file.
        content: str
            This will fetch data from rst file.
        return: str
            It returns rst in html format.
        '''
        title = self.options.get('title', 'EXPAND')
        content = self._parse_nested_content()
        #content = pattern.sub(link_replace_match, content)
        content = status_pattern.sub(status_replace_match, content)
        content = link_pattern.sub(link_replace_match,content)

        raw_html = f"""
        <ac:structured-macro ac:name="expand">
        <ac:parameter ac:name="title">{title}</ac:parameter>
        <ac:rich-text-body>{content}</ac:rich-text-body>
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
    '''Adding expand directive to add_directive'''
    app.add_directive('expand', ExpandDirective)
