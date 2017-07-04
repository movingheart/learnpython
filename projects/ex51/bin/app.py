# -*- coding:utf-8 -*-

import web

urls = (
    # '/', 'index',
    '/foo', 'foo',
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')



class index(object):
    def GET(self):
        # greeting = "Hello World!"
        greeting = u"你是我心内的一首歌！"
        return render.index(greeting=greeting)

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello")
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting=greeting)

class foo(object):
    def GET(self):
        lis = ["xiaoming", "xiaoli", "xiaofang"]
        return render.foo(var=lis)

if __name__ == "__main__":
    app.run()
