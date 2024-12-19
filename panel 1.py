'''This is Panel Macro custom directive'''

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from link import *

class PanelDirective(Directive):
    '''This custom directive class for panel which extends Directive class
    from sphinx library'''

    has_content = True
    final_argument_whitespace = True
    option_spec = {
        'title': directives.unchanged,
        'bordercolor': directives.unchanged,
        'borderstyle': directives.unchanged,
        'titlecolor': directives.unchanged,
    }
    def run(self):
        p_title= self.options.get('title', None)
        border_color = self.options.get('bordercolor', 'black')
        border_style = self.options.get('borderstyle', 'solid')
        title_color = self.options.get('titlecolor', 'black')
        content = self._parse_nested_content()

        #content = pattern.sub(link_replace_match, content)
        content = status_pattern.sub(status_replace_match,content)
        content = link_pattern.sub(link_replace_match,content)
        content = image_pattern.sub(image_replace_match,content)
        content = children_pattern.sub(children_replace_match,content)
        content = contentBylabel_pattern.sub(content_replace_match,content)

        raw_html = f"""
                <ac:structured-macro ac:name="panel" ac:schema-version="1">
                    <ac:parameter ac:name="title">{p_title}</ac:parameter>
                    <ac:parameter ac:name="borderColor">{border_color}</ac:parameter>
                    <ac:parameter ac:name="borderStyle">{border_style}</ac:parameter>
                    <ac:parameter ac:name="titleColor">white</ac:parameter>
                    <ac:parameter ac:name="titleBGColor">{title_color}</ac:parameter>
                    <ac:parameter ac:name="width">25px</ac:parameter>
                        <ac:rich-text-body> {content}</ac:rich-text-body>
                </ac:structured-macro>
        """
        raw_node = nodes.raw('', raw_html, format='html')
        return [raw_node]

    def _parse_nested_content(self):
        #env = self.state.document.settings.env
        node = nodes.Element()
        self.state.nested_parse(self.content, self.content_offset, node)
        return ''.join(node.astext())

def setup(app):
    '''Adding expand directive to add_directive'''
    app.add_directive('panel', PanelDirective)
