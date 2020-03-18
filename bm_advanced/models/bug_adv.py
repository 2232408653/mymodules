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
    @api.onchange('user_id')
    def user_follower_ref(self):
        if not self.user_id:
            self.follower_id = None
        return{
            'warning':{
                'title':'无负责人',
                'message':'关注者也被清空'
            }
        }
    ''':arg
    本例中，我们使用@api.onchange装饰器来绑定follower_id和user_id之间的处理逻辑，
    这样就可以监控user_id的变化来触发对follower_id的动作。
    需要注意的是，这个方法的具体名字与方法的触发没有直接关联性，Odoo主要是通过方法的装饰器来找到方法的。
    在onchange方法中，参数self代表的是包含了form所有可编辑字段的单一记录，
    我们可以对这些字段进行操作。
    一般来说，onchange可以非常方便地根据一些字段的变化对其他字段进行进一步的赋值等操作。
    '''
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