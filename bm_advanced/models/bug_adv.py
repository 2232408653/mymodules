# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BugAdvanced(models.Model):
    _inherit='ds_bug'
    #进阶模型当中新增一个所需时间字段
    need_time=fields.Integer('所需时间(小时)')
    #给bm.bug类的name字段增加help属性
    name=fields.Char(help='简要描述发现的bug')
    stage_id=fields.Many2one('bm_bug_stage','阶段')
    tag_ids=fields.Many2many('bm_bug_tag',string='标示')
# # -*- coding: utf-8 -*-
#
# from odoo import models, fields, api
#
# class bugAdvance(models.Model):
#     #使用_inherit模型属性继承了ds_bug模型
#     ''':arg
#     本模型并没有使用_name属性，
#     这就证明该模型后续的修改相当于是使用了ds_bug作为名字，
#     只是基于该模型进行修改。
#     '''
#     _inherit = 'ds_bug'
#     ##在进阶模型中新增一个所需的时间字段
#     need_time = fields.Integer('所需时间(小时)')
#     # 为ds_bug类的name字段增加help属性
#     name = fields.Char(help='简要描述发现的bug')
#
#     stage_id = fields.Many2one('bm.bug_tag','阶段')
#     tag_ids = fields.Many2many('bm.bug_tag', string='标示')