# -*- coding: utf-8 -*-
from odoo import http


class Main(http.Controller):
    @http.route('/helloworld', auth='public')
    def hello_world(self):
        return ('<h1>Hello World!</h1>')

# class BmWebsite(http.Controller):
#     @http.route('/bm_website/bm_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bm_website/bm_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bm_website.listing', {
#             'root': '/bm_website/bm_website',
#             'objects': http.request.env['bm_website.bm_website'].search([]),
#         })

#     @http.route('/bm_website/bm_website/objects/<model("bm_website.bm_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bm_website.object', {
#             'object': obj
#         })
