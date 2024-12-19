from docutils.parsers.rst import Directive
from docutils import nodes
import openpyxl

class ConfluencePanel(Directive):
    has_content = True
    option_spec = {
        'file': str,
        'sheet': str
    }

    def run(self):
       
        file_path = self.options.get('file', './excel_file1.xlsx')
        sheet_name = self.options.get('sheet', None)
        wb = openpyxl.load_workbook(file_path)
        if sheet_name:
            ws = wb[sheet_name]
        else:
            ws = wb.active

             
        for content in ws.iter_rows(values_only=True):
            content1 = content[0] if len(content) > 0 else ""
            content2 = content[1] if len(content) > 1 else ""
            content3 = content[2] if len(content) > 2 else ""
            content4 = content[3] if len(content) > 3 else ""
        

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
    app.add_directive('confluence-panel_xl', ConfluencePanel)
    return {'version': '1.0', 'parallel_read_safe': True}
