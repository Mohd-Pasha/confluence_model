from docutils import nodes
from docutils.parsers.rst import Directive

class MultiSectionDirective(Directive):
    has_content = True

    def run(self):
        # Access the content
        content = '\n'.join(self.content)
        # Split the content to get macro one by one
        content = content.split('===')

        # Create one section with type single
        raw_html_part_1 = f"""
        <ac:structured-macro ac:name="section">
        <ac:rich-text-body>"""

        # Closing the section
        raw_html_part_2 = f"""
        </ac:rich-text-body>
        </ac:structured-macro>"""

        content_len = len(content)
        width = 100 // content_len
        count = 0

        # To add multiple columns in the above section
        while content_len != count:
            for column in range(len(content)):
                res_content = content[column].strip() if len(content) > 0 else ""
                temp_column = f"""
                <ac:structured-macro ac:name="column">
                <ac:parameter ac:name="width">{width}%</ac:parameter>
                <ac:rich-text-body>
                <div style="border: 1px solid black; color: yellow; background-color: grey;">
                {res_content}
                </div>
                </ac:rich-text-body>
                </ac:structured-macro>"""
                raw_html_part_1 += temp_column
                content_len -= 1

        raw_html = raw_html_part_1 + raw_html_part_2

        # Returning the macro in HTML format
        raw_node = nodes.raw('', raw_html, format='html')
        return [raw_node]

# Example usage: Registering the directive if needed
def setup(app):
    app.add_directive('multi-section', MultiSectionDirective)
