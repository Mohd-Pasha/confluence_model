from docutils.parsers.rst import Directive
from docutils import nodes

class Confluence1(Directive):
    has_content = True

    def run(self):
        
        
        content = self.content
        #Storing content in the form of string List.
        
       
        Point = "<ul>"

        for line in content:

            #iterating each element and adding inside the bullet html tag. 
            Point += f"<li>{line.strip()}</li>"
        Point += "</ul>"
        #Final Point is containing all the Bullet point tags.

        
        raw_node = nodes.raw('', Point, format='html')
        #converting again the whole Point format into html.
        return [raw_node]

def setup(app):
    app.add_directive('bullets', Confluence1)
    return {'version': '1.0', 'parallel_read_safe': True}
