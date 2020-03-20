from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/bugs', auth='user', website=True)
    def index(self, **kwargs):
        Bugs = request.env['ds_bug']
        bugs = Bugs.search([])
        return request.render(
            'bm_website.index',
            {'bugs': bugs})

    # @http.route('/bug/<model("bm.bug"):bug>',
    #             auth="user",  # 默认为user, 但是我们显示指定
    #             website=True)
    # def detail(self, bug, **kwargs):
    #     return http.request.render(
    #         'bm-website.detail',
    #         {'bug': bug})
    #
    # @http.route('/bug/add', auth="user", website=True)
    # def add(self, **kwargs):
    #     users = request.env['res.users'].search([])
    #     return request.render(
    #         'bm-website.add', {'users': users})
