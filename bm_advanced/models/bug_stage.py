# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugStage(models.Model):
    _name = 'bm_bug_stage'
    _description = 'bug阶段'
    _order = 'sequence,name'

    name = fields.Char('名称')
    des_detail = fields.Char('名称')
    '''
    Selection（items，string）：这是下拉列表框，
    在前面的章节中已经使用过。
    第一个参数是可选的选项列表，
    列表内通过元组来标示每一行的选项。
    String是前端展示时的字段描述。
    '''
    status = fields.Selection([('wating','未开始'),('doing','进行中'),('closed','关闭'),('rework','重测未通过')],'状态')
    document =fields.Html('文档')
    sequence = fields.Integer('Sequence')
    precent_pro = fields.Float('进度',(3,2))
    '''
    Float（string，digits）：string仍然是前端显示时该字段的描述，
    digits是一个元组，
    前面的数代表该数字的总位数，
    后面的数字则代表小数精度。
    '''
    deadline = fields.Date('最晚解决日期')
    creat_on = fields.Datetime('创建时间',default=lambda self:fields.Datetime.now())
    delay = fields.Boolean('是否延误')
    image=fields.Binary('图片')
    '''
    常用的字段属性关键字
    string：前端展现时的字段描述属性，
        除了Selection和关系字段之外，
        该属性都是出现在字段内的第一个位置，
        所以最常见的通过位置使用的属性就是该属性。
    default：字段的默认值属性，
        可以是静态值也可以是匿名函数等。
        上例中的create_on字段就是使用lambda函数给出默认值。
    size：仅在Char字段中有效，
        可用于限制最大字符数，
        比如身份证号的最大长度。
    translate：在Char、Text和Html字段中起作用，
        使本字段可翻译。
    help：进行前端展示时，发送给用户的提示信息。
    readonly：默认为False，
        如果设置为True则在前端不可编辑，
        在模型层通过函数更改数据不会受到影响。
    required：设置为True则表示在前端使用时本字段不可为空，
        此项设置对模型层也是有作用的，相当于是在数据库表的字段上进行了非空设置，
        使用函数在模型里面写入该字段为空的记录也会受到限制。
    index：如果设置为True则会在对应的数据库字段上添加索引，
        会提升按该字段进行查询时的效率，同时降低写数据库表的速度。
    copy：默认非关系字段是True，如果设置为False则在复制记录时，该字段不被复制。
    groups：该字段属性用于限定该字段的访问安全组，
        通过外部ID进行指定即可访问的安全组，多个外部id之间可以用逗号隔开，
        比如，groups='base.group_portal，base.group_user'。
    states：该属性是通过字典来设置UI的相关属性，
        readonly、required和invisible三个属性都可以通过该属性进行设置，
        比如将字段设置为只读states={'done'：['readonly'，True]}。
        视图中的attr属性与该属性类似，不过attr主要用于根据不同情况切换可见性等应用。
    deprecated：如果设置为True，则一旦使用该字段，
        就会在日志中记录警告信息。
    oldname：如果一个字段在新版本中更改了名字，
        则可以使用该属性记录老版本的名字，
        这种设置可以在复制记录时使得老版本的数据字段自动复制到对应的新名字字段。
    '''
    '''
    其他特殊字段
    active：是一个布尔类型字段，允许通过该字段将记录设置为非激活状态，
        如果设置了active=False，
        则在前端查询时该记录会被自动排除在外，
        这一点类似于逻辑删除。
        当然也可以通过域（domain）设置查询active=True的记录。
    sequence：是Integer类型的字段，
        如果出现在列表视图则允许我们手动拖动记录来定义记录的顺序。
        如果要使用该字段，那么不要忘记在模型属性_order中引入该字段。
    state：Selection类型，其代表了记录生命周期的基本状态，
        并且可以通过该属性来动态修改视图；
        一些表单视图字段可以在特定记录状态指定readonly、required和invisible的具体值。
    parent_id、parent_left、parent_right：Integer类型，
        在层级关系中具有特殊的意义。本章后续会具体介绍层级关系。
    '''
    bug_ids = fields.One2many('ds_bug', 'stage_id', sting='bug')
    bug_ids = fields.Many2many('ds_bug', string='bug')
    