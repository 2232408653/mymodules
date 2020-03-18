# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bugWizard(models.TransientModel):
    _name = 'bug_wizard'
    bug_ids = fields.Many2many('ds_bug', string='Bug')
    new_is_closed = fields.Many2one('res.users',string='负责人')
    wizard_user_id = fields.Many2one('res.users', string='负责人')
    ''':arg
    我们可以借助context来完成default_get()方法。当视图的一些元素发生一些动作时，
    比如点击或跳转，这些元素将被添加到context字典中，常用的元素具体如下。
        active_model：记录视图模型的技术名称。
        active_id：如果是表单视图则记录活跃状态的记录ID，如果是列表视图则记录第一条记录的ID。
        active_ids：列表视图所有活跃状态的记录ID，如果是表单视图则只记录一个元素。
    '''
    @api.model
    def default_get(self, fields_names):
        defaults=super(bugWizard,self).default_get(fields_names)
        defaults['bug_ids']=self.env.context['active_ids']
        return defaults