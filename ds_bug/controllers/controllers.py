# -*- coding: utf-8 -*-
from odoo import http
'''
'''
class Bug(http.Controller):

    @http.route('/bug-manage')
    def BugManage(self, **kwargs):
        bugs=http.request.env['ds_bug']
        domain_bug=[('is_closed','=',False)]
        bugs_open=bugs.search(domain_bug)
        return http.request.render('ds_bug.bugs_template',{'bugs_open':bugs_open})
# class DsBug(http.Controller):
#     @http.route('/ds_bug/ds_bug/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ds_bug/ds_bug/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ds_bug.listing', {
#             'root': '/ds_bug/ds_bug',
#             'objects': http.request.env['ds_bug.ds_bug'].search([]),
#         })

#     @http.route('/ds_bug/ds_bug/objects/<model("ds_bug.ds_bug"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ds_bug.object', {
#             'object': obj
#         })