# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bug(models.Model):
    _name = "ds_bug"
    _description = "bug"
    name = fields.Char('bug简述',required=True)
    detail = fields.Text(size=150)
    is_closed = fields.Boolean("是否关闭")
    close_reason = fields.Selection([('changed','已修改'),('cannot','无法修改'),('delay','推迟')],string='关闭理由')
    user_id = fields.Many2one('res.users',string='负责人')
    follower_id = fields.Many2one('res.partner',string="关注者")
    '''
    _name:类的唯一标识字段,其它类可以通过此字段引用本类
    _description:类似于标签,提高查询的友好性
    name:特殊字段,其作用类似于3.3.4节介绍的x_name字段,其他模型引用时name作为标题
    属性required = True 代表该字段为必输入字段
    datail:文本字段.可通过size属性定义其长度为150
    '''
    '''
    字段的常用属性:
    string：在前端界面看到的字段名称，默认是字段的技术名称。
    required：默认是False，如果设置成True，则在创建记录时该字段不允许为空。
    help：在前端使用时作为提示信息。
    index：布尔类型，默认为False。如果是True则会在数据库的该字段上创建索引。
    '''
    '''
    保留字段:
    在模型里面，有一些字段是系统保留的，作为开发人员不能修改这些字段，这些保留字段具体如下。
    id：这是记录的唯一标示。
    create_date：记录创建的日期。
    create_uid：Many2one类型，创建该记录的用户。
    ·write_date：记录的最后修改日期。
    write_uid：Many2one类型，记录的最后修改用户。
    _last_upadte：该字段并不会实际存储值，其在这里仅起到并发检查的作用。
    如果要查看以上字段的具体值，则可以在前端开发模式下，通过debug按钮的查看元数据选项查看数据明细。
    注:
    name字段是模型里面的特殊字段，在默认情况下该字段的值可用来在搜索和引用时代表一行记录。
    '''

    @api.multi
    def do_close(self):
        for item in self:
            item.is_closed = True
        return True
