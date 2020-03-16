# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugStage(models.Model):
    _name = 'bm_bug_stage'
    _description = 'bug阶段'
    _order = 'sequence,name'

    name = fields.Char('名称')
    sequence = fields.Integer('Sequence')
    