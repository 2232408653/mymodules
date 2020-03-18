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
    onchange方法不需要返回任何参数，不过我们可以选择通过返回一个字典来返回一个warning或者domain。
    warning关键字应该给出一个信息用于返回到弹出对话框，比如：
    1.    {'title': 'Message Title', 'message': 'Message Body'}  
    domain关键字可以修改字段的domain属性，这样做会提高用户使用时的友好性，
    比如，我们在选择关注者的时候，可以仅允许用户从联系人中选择教师，写出来形式大概如下：
    1.    {'follower_id': [('x_is_teacher', '=', True)]}  
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