from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/helloworld', auth='public')
    def hello_world(self):
        return ('<h1>Hello World!</h1>')

    @http.route('/hello', auth='public')
    def hello(self, **kwargs):
        return request.render('bm_website.hello')

    @http.route('/bugs', auth='user', website=True)
    def index(self, **kwargs):
        Bugs = request.env['ds_bug']
        bugs = Bugs.search([])
        return request.render(
            'bm_website.index',
            {'bugs': bugs})

    '''
    控制器检索要使用的数据并使其可用于呈现的模板。
    在这种情况下，控制器需要经过身份验证的会话，因为该路由具有auth='user'属性。
    这是默认的行为，显式声明需要用户会话是一种很好的做法。
    用户登录后，bugs的search()语句将在该上下文中运行并返回相应的记录。
    '''
    '''
    对于不需要经过身份验证访问的控制器，可以读取的数据非常有限。
    在这种情况下，我们通常需要在上下文中运行部分代码。
    为此，可以使用sudo()模型方法，它能将安全上下文更改为Admin用户，这样就删除了大多数限制。
    '''
    '''
    请注意，路由使用带有模型（"ds_bug"）转换器的占位符，
    该转换器将映射到方法的bug参数上。其将从URL捕获bug标识符，
    可以是简单的ID号或分段标示，并将其转换为相应的浏览记录对象。
    '''
    @http.route('/bug/<model("ds_bug"):bug>',
                auth="user",  # 默认为user, 但是我们显示指定
                website=True)
    def detail(self, bug, **kwargs):
        return http.request.render(
            'bm_website.detail',
            {'bug': bug})
    ''':arg
    这是一个简单的控制器，生成一个新的自定义bug-website.add模板，
    并为其提供用户列表，以便它们可用于选择框的构建。
    '''
    @http.route('/bug/add', auth="user", website=True)
    def add(self, **kwargs):
        users = request.env['res.users'].search([])
        return request.render(
            'bm_website.add', {'users': users})
