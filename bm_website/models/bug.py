from odoo import api, models,fields
from odoo.exceptions import ValidationError

class Bug(models.Model):
    _inherit = 'ds_bug'
    deadline = fields.Date('最晚解决日期')

    @api.model
    def website_form_input_filter(self, request, values):
        if values.get('name'):
            # Modify values
            values['name'] = values['name'].strip()
            # Validate values
            if len(values['name']) < 3:
                raise ValidationError(
                    '名称长度不可以少于3个字符')
        return values