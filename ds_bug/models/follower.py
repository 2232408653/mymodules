# -*- coding: utf-8 -*-

from odoo import models, fields, api


class flowwer(models.Model):
    _inherit = 'res.partner'
    bug_ids = fields.Many2many('ds_bug', string='bug')
