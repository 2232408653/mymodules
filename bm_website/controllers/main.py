from odoo import http
from odoo.http import request

class Main(http.Controller):
    @http.route('/helloworld', auth='public')
    def hello_world(self):
        return ('<h1>Hello World!</h1>')

    @http.route('/hello',auth='public')
    def hello(self,**kwargs):
        return request.render('bm_website.hello')

    @http.route('/bugs', auth='user', website=True)
    def index(self, **kwargs):
        Bugs = request.env['ds_bug']
        bugs = Bugs.search([])
        return request.render(
            'bm_website.index',
            {'bugs': bugs})

    @http.route('/bug/<model("ds_bug"):bug>',
                auth="user",  # 默认为user, 但是我们显示指定
                website=True)
    def detail(self, bug, **kwargs):
        return http.request.render(
            'bm_website.detail',
            {'bug': bug})

    @http.route('/bug/add', auth="user", website=True)
    def add(self, **kwargs):
        users = request.env['res.users'].search([])
        return request.render(
            'bm_website.add', {'users': users})