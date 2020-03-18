# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bugWizard(models.TransientModel):
    _name = 'bug_wizard'
    bug_ids = fields.Many2many('ds_bug', string='Bug')
    new_is_closed = fields.Many2one('res.users',string='负责人')
