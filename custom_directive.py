from docutils.parsers.rst import Directive
from docutils import nodes

class ConfluencePanel(Directive):
    
    has_content = True
    
    

    def run(self):
        content='\n\n\n'.join(self.content)
        panel = f"""
        <ac:structured-macro ac:name="panel">
            <ac:parameter ac:name="title">Important Notice</ac:parameter>
            <ac:parameter ac:name="borderStyle">solid</ac:parameter>
            <ac:parameter ac:name="borderColor">blue</ac:parameter>
            <ac:parameter ac:name="backgroundColor">blue</ac:parameter>
                <ac:rich-text-body>
                   {content}
               </ac:rich-text-body>
                </ac:rich-text-body>
        </ac:structured-macro>
        <ac:structured-macro ac:name="panel">
            <ac:parameter ac:name="title">Important Notice</ac:parameter>
            <ac:parameter ac:name="borderStyle">solid</ac:parameter>
            <ac:parameter ac:name="borderColor">blue</ac:parameter>
            <ac:parameter ac:name="backgroundColor">blue</ac:parameter>
                <ac:rich-text-body>
                   {content}
               </ac:rich-text-body>
                </ac:rich-text-body>
        </ac:structured-macro>
        """
        raw_node = nodes.raw('', panel, format='html')
        
        return [raw_node]

def setup(app):
    app.add_directive('confluence-panel', ConfluencePanel)
    return {'version':'1,0','parallel_read_safe':True}

