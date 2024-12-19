from docutils.parsers.rst import Directive
from docutils import nodes
import subprocess

class ConfluenceComment(Directive):
    has_content = True

    def run(self):
        # Join the content lines from the reST file
        content = '\n'.join(self.content)
        
        # Page ID should be provided in the directive options or content
        page_id = "123456"  # Replace with the actual page ID or get it from options
        
        # Call the Python script to add the comment
        script_path = "path/to/your/script.py"  # Replace with the actual script path
        
        result = subprocess.run(
                ["python", script_path, page_id, content],
                capture_output=True,
                text=True
            )
           

        # Indicate success in the generated document
        success_msg = f"Comment added to Confluence page {page_id}."
        paragraph_node = nodes.paragraph(text=success_msg)
        return [paragraph_node]

def setup(app):
    app.add_directive('confluence-comment', ConfluenceComment)
    return {'version': '1.0', 'parallel_read_safe': True}
