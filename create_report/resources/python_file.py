# report file def

def get_report_def(report_name, file_name, module_name,model_name, odoov):
    # formated file name ex: report_name -> ReportName
    formated_file_name = "".join((list(map(lambda x: x.capitalize() ,file_name.replace('.py','').split('_')))))
    content = ''
    if odoov == 10:
        content = \
"""
        pending development... sorry :c
"""
    else:
        content = \
"""# -*- encoding: utf-8 -*-
##################################################################################################
#
#   Author: Experts SAS (www.experts.com.mx)
#   Coded by: Daniel Acosta (daniel.acosta@experts.com.mx)
#   License: https://blog.experts.com.mx/licencia-de-uso-de-software/
#
##################################################################################################
from odoo import api, fields, models, _, tools
from odoo.exceptions import UserError

class """+formated_file_name+"""(models.Model):
    # _name must be report.module_name.template_id
    _name = 'report."""+module_name+"""."""+report_name+"""'

    @api.model
    def _get_report_values(self, docids, data=None):
        # if data is None is not called from button
        data = data if data is not None else {'active_id': self._context.get('active_ids'), 'active_model': self._context.get('active_model')}
        ids = data.get('active_ids',docids)
        doc_model = data.get('active_model','"""+model_name+"""')
        docs = self.env[doc_model].browse(ids)
        return {
            'doc_ids': ids,
            'doc_model': doc_model,
            'docs': docs,
            'self': self,
            'data': dict(
                data,
            ),
        }"""
    return content