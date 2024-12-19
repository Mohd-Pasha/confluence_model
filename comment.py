from docutils import nodes
from docutils.parsers.rst import Directive, directives

class VersionCommentDirective(Directive):
   
    has_content = True

    def run(self):
        
        comment_text = '\n'.join(self.content) 
       
        para = nodes.paragraph(text=comment_text)
        return [para]



def setup(app):
    app.add_directive('v_c', VersionCommentDirective)
    return {'version':'1,0','parallel_read_safe':True}

