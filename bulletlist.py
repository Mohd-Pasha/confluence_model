from docutils import nodes
from docutils.parsers.rst import Directive

class BulletListDirective(Directive):
    # The directive has content
    has_content = True

    def run(self):
        # Create a raw node for Confluence Storage Format
        raw_node = nodes.raw('', self.create_bullet_list(), format='html')
        return [raw_node]

    def create_bullet_list(self):
        # Generate Confluence Storage Format bullet list
        bullet_list = '<ul>'
        for item in self.content:
            bullet_list += f'<li>{item.strip()} </li>'
        bullet_list += ' </ul>'
        return bullet_list

def setup(app):
    app.add_directive("bulletlist", BulletListDirective)
