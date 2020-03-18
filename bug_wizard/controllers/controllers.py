# -*- coding: utf-8 -*-
from odoo import http

# class BugWizard(http.Controller):
#     @http.route('/bug_wizard/bug_wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bug_wizard/bug_wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bug_wizard.listing', {
#             'root': '/bug_wizard/bug_wizard',
#             'objects': http.request.env['bug_wizard.bug_wizard'].search([]),
#         })

#     @http.route('/bug_wizard/bug_wizard/objects/<model("bug_wizard.bug_wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug_wizard.object', {
#             'object': obj
#         })