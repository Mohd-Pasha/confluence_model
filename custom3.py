from docutils.parsers.rst import Directive
from docutils import nodes

class ConfluencePanel(Directive):
    has_content = True

    def run(self):
        # Join the content and split based on the delimiter `===`
        content = '\n'.join(self.content)
        parts = content.split('===')
        content1 = parts[0].strip() if len(parts) > 0 else ""
        content2 = parts[1].strip() if len(parts) > 1 else ""
        content3 = parts[2].strip() if len(parts) > 0 else ""
        content4 = parts[3].strip() if len(parts) > 1 else ""

        panel = f"""
        <ac:structured-macro ac:name="section" ac:schema-version="1" >
            <ac:parameter ac:name="width">100%</ac:parameter>
            
            <ac:rich-text-body>
                <ac:structured-macro ac:name="column" ac:schema-version="1">
                    <ac:parameter ac:name="width">25%</ac:parameter>
                       <ac:rich-text-body>
                        
                        <ac:structured-macro ac:name="panel" ac:schema-version="1">
                                <ac:parameter ac:name="title">User details </ac:parameter>
                                <ac:parameter ac:name="borderStyle">solid</ac:parameter>
                                <ac:parameter ac:name="borderColor">black</ac:parameter>
                                <ac:parameter ac:name="bgColor">white</ac:parameter>
                                <ac:parameter ac:name="titleBGColor">yellow</ac:parameter>
                                <ac:rich-text-body>
                                   {content1}
                                </ac:rich-text-body>
                        </ac:structured-macro>
                       </ac:rich-text-body>
                </ac:structured-macro>
                <ac:structured-macro ac:name="column" ac:schema-version="1" >
                    <ac:parameter ac:name="width">25%</ac:parameter>
                        <ac:rich-text-body>
                         
                         <ac:structured-macro ac:name="panel" ac:schema-version="1">
                                <ac:parameter ac:name="title">User 2 details</ac:parameter>
                                <ac:parameter ac:name="borderStyle">solid</ac:parameter>
                                <ac:parameter ac:name="borderColor">black</ac:parameter>
                                <ac:parameter ac:name="bgColor">white</ac:parameter>
                                <ac:parameter ac:name="titleBGColor">yellow</ac:parameter>
                                <ac:rich-text-body>
                                    {content2}
                                </ac:rich-text-body>
                         </ac:structured-macro>
                         
                        </ac:rich-text-body>
                </ac:structured-macro>
                <ac:structured-macro ac:name="column" ac:schema-version="1">
                    <ac:parameter ac:name="width">25%</ac:parameter>
                       <ac:rich-text-body>
                        
                         <ac:structured-macro ac:name="panel" ac:schema-version="1">
                                <ac:parameter ac:name="title">SW</ac:parameter>
                                <ac:parameter ac:name="borderStyle">solid</ac:parameter>
                                <ac:parameter ac:name="borderColor">black</ac:parameter>
                                <ac:parameter ac:name="bgColor">white</ac:parameter>
                                <ac:parameter ac:name="titleBGColor">yellow</ac:parameter>
                                    <ac:rich-text-body>
                                    {content3}
                                </ac:rich-text-body>
                         </ac:structured-macro>
                       </ac:rich-text-body>
                    </ac:structured-macro>
                <ac:structured-macro ac:name="column" ac:schema-version="1" >
                    <ac:parameter ac:name="width">25%</ac:parameter>
                        <ac:rich-text-body>
                         
                         <ac:structured-macro ac:name="panel" ac:schema-version="1">
                                <ac:parameter ac:name="title">Panel</ac:parameter>
                                <ac:parameter ac:name="borderStyle">solid</ac:parameter>
                                <ac:parameter ac:name="borderColor">black</ac:parameter>
                                <ac:parameter ac:name="bgColor">white</ac:parameter>
                                <ac:parameter ac:name="titleBGColor">yellow</ac:parameter>
                                <ac:rich-text-body>
                                  {content4}
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
    app.add_directive('confluence-panel_moin', ConfluencePanel)
    return {'version': '1.0', 'parallel_read_safe': True}
