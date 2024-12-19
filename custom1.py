from docutils.parsers.rst import Directive
from docutils import nodes

class ConfluencePanel(Directive):
    
    has_content = True
    
    

    def run(self):

        
        panel = f"""
        
         <ac:structured-macro ac:name="section" ac:schema-version="1" >
            <ac:parameter ac:name="width">100%</ac:parameter>
            
            <ac:rich-text-body>
                <ac:structured-macro ac:name="column" ac:schema-version="1">
                    <ac:parameter ac:name="width">25%</ac:parameter>
                       <ac:rich-text-body>
                        Hello Moin
                        <ac:structured-macro ac:name="panel" ac:schema-version="1">
                                <ac:parameter ac:name="title">Panel 1 Macro using md directive</ac:parameter>
                                <ac:parameter ac:name="borderStyle">solid</ac:parameter>
                                <ac:parameter ac:name="borderColor">black</ac:parameter>
                                <ac:parameter ac:name="bgColor">white</ac:parameter>
                                <ac:parameter ac:name="titleBGColor">yellow</ac:parameter>
                                <ac:rich-text-body>
                                    <h3>MACROS CONTENT</h3>
                                    <p>This is the content inside the panel macro.</p>
                                    <p>A software factory is a structured collection of related software assets that aids in producing computer software applications or software components according to specific, externally defined end-user requirements through an assembly process.</p>
                                </ac:rich-text-body>
                        </ac:structured-macro>
                       </ac:rich-text-body>
                </ac:structured-macro>
                <ac:structured-macro ac:name="column" ac:schema-version="1" >
                    <ac:parameter ac:name="width">25%</ac:parameter>
                        <ac:rich-text-body>
                         Hello anjali
                         <ac:structured-macro ac:name="panel" ac:schema-version="1">
                                <ac:parameter ac:name="title">Panel 1 Macro using md directive</ac:parameter>
                                <ac:parameter ac:name="borderStyle">solid</ac:parameter>
                                <ac:parameter ac:name="borderColor">black</ac:parameter>
                                <ac:parameter ac:name="bgColor">white</ac:parameter>
                                <ac:parameter ac:name="titleBGColor">yellow</ac:parameter>
                                <ac:rich-text-body>
                                    <h3>MACROS CONTENT</h3>
                                    <p>This is the content inside the panel macro.</p>
                                </ac:rich-text-body>
                         </ac:structured-macro>
                         
                        </ac:rich-text-body>
                </ac:structured-macro>
                <ac:structured-macro ac:name="column" ac:schema-version="1">
                    <ac:parameter ac:name="width">25%</ac:parameter>
                       <ac:rich-text-body>
                        Hello Moin
                         <ac:structured-macro ac:name="panel" ac:schema-version="1">
                                <ac:parameter ac:name="title">Panel 1 Macro using md directive</ac:parameter>
                                <ac:parameter ac:name="borderStyle">solid</ac:parameter>
                                <ac:parameter ac:name="borderColor">black</ac:parameter>
                                <ac:parameter ac:name="bgColor">white</ac:parameter>
                                <ac:parameter ac:name="titleBGColor">yellow</ac:parameter>
                                <ac:rich-text-body>
                                    <h3>MACROS CONTENT</h3>
                                    <p>This is the content inside the panel macro.</p>
                                </ac:rich-text-body>
                         </ac:structured-macro>
                       </ac:rich-text-body>
                    </ac:structured-macro>
                <ac:structured-macro ac:name="column" ac:schema-version="1" >
                    <ac:parameter ac:name="width">25%</ac:parameter>
                        <ac:rich-text-body>
                         Hello anjali
                         <ac:structured-macro ac:name="panel" ac:schema-version="1">
                                <ac:parameter ac:name="title">Panel 1 Macro using md directive</ac:parameter>
                                <ac:parameter ac:name="borderStyle">solid</ac:parameter>
                                <ac:parameter ac:name="borderColor">black</ac:parameter>
                                <ac:parameter ac:name="bgColor">white</ac:parameter>
                                <ac:parameter ac:name="titleBGColor">yellow</ac:parameter>
                                <ac:rich-text-body>
                                    <h3>MACROS CONTENT</h3>
                                    <p>This is the content inside the panel macro.</p>
                                </ac:rich-text-body>
                         </ac:structured-macro>
                         
                        </ac:rich-text-body>
                </ac:structured-macro>
            </ac:rich-text-body>
         </ac:structured-macro>
        

        """
        raw_node = nodes.raw('', panel, format='html')
        
        return [raw_node]

def setup(app):
    app.add_directive('confluence-panel1', ConfluencePanel)
    return {'version':'1,0','parallel_read_safe':True}

