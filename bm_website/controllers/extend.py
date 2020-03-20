from odoo import http
#from odoo.addons.bm-website.controllers.main import Main
#python  不支持减号作为模块的目录名和文件名， 使用如下方法绕过这一限制
import importlib
Main = importlib.import_module("odoo.addons.bm_website.controllers.controllers").Main
class MainExtended(Main):

    @http.route()
    def hello(self, name=None, **kwargs):
        response = super(MainExtended, self).hello()
        response.qcontext['name'] = name
        #print(name)
        return response
    @http.route(['/hello','/hello/<name>'])
    def hello(self,name=None,**kwargs):
        response = super(MainExtended, self).hello()
        response.qcontext['name'] = name
        # print(name)
        return response

    @http.route('/hellocms/<page>', auth='public')
    def hello(self, page, **kwargs):
        print(page)
        return http.request.render(page)