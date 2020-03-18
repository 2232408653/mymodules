# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging
_logger=logging.getLogger(__name__)


class bugWizard(models.TransientModel):
    _name = 'bug_wizard'
    bug_ids = fields.Many2many('ds_bug', string='Bug')
    new_is_closed = fields.Boolean('是否关闭')
    wizard_user_id=fields.Many2one('res.users',string='负责人')
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
    '''
    该方法每次处理一个向导实例，所以使用了self.ensure_one()方法。此处的self代表了在向导视图中正在浏览的记录。
    方法首先验证了在向导窗口中是否有负责人或是否关闭的新值，如果没有则会报错，事实上若两个值都没有的话，
    那么此批量更新按钮就不会出现。然后用字典存储两个字段的值，使用模型的写入方法一次性写入。
    方法的最后会返回一个True值，虽然这不是必需的，但读者最好养成这种代码书写习惯。
    '''
    @api.multi
    def update_batch(self):
        self.ensure_one()
        if not (self.new_is_closed or self.wizard_user_id):
            raise exceptions.ValidationError('无数据要更新')
        '''
        使用了_logger，该对象需要在models/bug_wizard.py文件内声明引入，所以需要在类的前面增加如下两行代码：
        1.    import logging  
        2.    _logger=logging.getLogger(__name__) 
        关于logging的使用，需要做一下介绍，为什么要在此处增加日志信息记录呢？因为上例中的批量更新操作，
        很容易对某些记录进行误选，通过日志记录下来以便于复查。
        在上面的代码中，_logger是用标准库进行初始化的，
        而且是在bugWizard类之前。Python内部变量__name__用于标示日志信息来自于本模块。
        在代码中写下日志消息，可以使用如下四种方法：
           1.    _logger.debug('DEBUG 信息')  
           2.    _logger.info('INFO信息')  
           3.    _logger.warning('WARNING信息')  
           4.    _logger.error('ERROR信息')   
        '''
        _logger.debug('批量bug更新操作 %s',self.bug_ids.ids)
        vals={}
        if self.new_is_closed:
            vals['is_closed'] = self.new_is_closed
        if self.wizard_user_id:
            vals['user_id'] = self.wizard_user_id.id
        if vals:
            self.bug_ids.write(vals)
        return True
    @api.multi
    def count_bugs(self):
        bug=self.env['ds_bug']
        count = bug.search_count([])
        raise exceptions.Warning('有%d条bug'%count)

    @api.multi
    def helper_form(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,  # this model
            'res_id': self.id,  # the current wizard record
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'}

    @api.multi
    def get_bugs(self):
        self.ensure_one()
        bug = self.env['ds_bug']
        all_bugs = bug.search([('is_closed', '=', False)])
        # Fill the wizard Task list with all tasks
        self.bug_ids = all_bugs
        # reopen wizard form on same wizard record
        return self.helper_form()