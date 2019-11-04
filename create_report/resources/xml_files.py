import os
def get_template(report_name,module_name,odoov):
    content = ''
    if odoov == 10:
        content = \
"""
        pending development... sorry :c
"""
    else:
        content = \
'''<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>
        <template id="'''+report_name+'''_style">
          .page{
            font-family:Helvetica,Verdana,Arial,sans,Lucida Grande,Calibri;font-size:14px; width:100%;
          }
        </template>
        <template id="'''+report_name+'''">
            <t t-call="web.html_container">
                <t t-foreach="docs" t-as="doc">
                    <!-- page -->
                    <div class="page" style="">
                        <style type="text/css">
                            <t t-call="'''+module_name+'''.'''+report_name+'''_style"/>
                        </style>


                        <h1 style="color: #269982">Hello world, the report works!</h1> 
                        <hr/>
                        <h3><b>doc:</b><span t-esc="doc"/></h3>
                        <h3><b>doc_model:</b><span t-esc="doc_model"/></h3>
                        <h3><b>ids:</b><span t-esc="ids"/></h3>
                        <h3><b>self:</b><span t-esc="self"/></h3>
                        <h3><b>data:</b><span t-esc="data"/></h3>


                    </div> <!-- end page -->
                </t>
            </t>
        </template>
    </data>
</odoo>
'''
    return content

def get_paperstyle_format(module_name,report_name,model_name,model_string,odoov):
    module_name = str(module_name)
    report_name = str(report_name)
    model_name = str(model_name)
    model_string = str (model_string)
    content = ''
    if odoov == 10:
        content = \
"""
        pending development... sorry :c
"""
    else:
        content = \
'''<?xml version='1.0' encoding='utf-8'?>
<odoo>
    <data>
                 
        <!-- Define report node, name must be: '''+module_name+'''.template_id-->
        <record id="'''+report_name+'''_paperformat" model="report.paperformat">
            <field name="name">'''+report_name+'''_format</field>
            <field name="default" eval="True" />
            <field name="format">Letter</field>
            <field name="page_height">0</field>
            <field name="page_width">0</field>
            <field name="orientation">Portrait</field>
            <field name="margin_top">10</field>
            <field name="margin_bottom">10</field>
            <field name="margin_left">10</field>
            <field name="margin_right">10</field>
            <field name="header_line" eval="False" />
            <field name="header_spacing">10</field>
            <field name="dpi">90</field>
        </record>
        
        <report 
            id="'''+report_name+'''report_format"
            model="'''+model_name+'''"
            string="'''+model_string+'''"
            report_type="qweb-pdf"
            name="'''+module_name+'''.'''+report_name+'''"
            file="'''+module_name+'''.'''+report_name+'''"
            attachment_use="True"
            menu="True"
            print_report_name="object.name + '.pdf'"
        />
        
        <!-- Define action to report, attach the custom paper format -->
        <record id="'''+report_name+'''report_format" model="ir.actions.report">
            <field name="paperformat_id" ref="'''+module_name+'''.'''+report_name+'''_paperformat"/>
        </record>
        
    </data>
</odoo>
'''
    return content