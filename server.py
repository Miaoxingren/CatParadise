# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import random
import math
import os
import os.path
import data
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class ErrorHandler(tornado.web.RequestHandler):
    '''handler for error page'''
    def get(self):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('404.html')
        else:
            self.write('error:' + str(status_code))


class BookPartHandler(tornado.web.RequestHandler):
    def get(self, name):
        book = data.getbook(name)
        self.render('book-part.html', book=book, back_url='/book')


class BookHandler(tornado.web.RequestHandler):
    def get(self):
        all_img = data.getimages('book', 'books')
        book_img = all_img[:4]
        key = ['url', 'img', 'alt']
        books = []
        for x in range(4):
            books.append(dict(zip(key, ['/book/book'+str(x), book_img[x], str(x)])))
        self.render('book.html', books=books, back_url='/')


class SomaHandler(tornado.web.RequestHandler):
    def get(self):
        all_img = data.getimages('funnycat', 'funnycats')
        col = row = 2
        funnycats = []
        for x in range(col):
            funnycat = []
            for y in range(row):
                funnycat.append(all_img[random.randrange(0, 16)])
            funnycats.append(funnycat)
        bodyareas = data.getbodyareas()
        self.render('soma.html', funnycats=funnycats, bodyareas=bodyareas, back_url='/')


class SomaPartHandler(tornado.web.RequestHandler):
    def get(self, name):
        key = ['funnycat', 'title', 'details']
        val = []
        all_img = data.getimages('funnycat', 'funnycats')
        val.append(all_img[random.randrange(0, 16)])
        all_img = data.getimages('text-'+name, 'body')
        if len(all_img) < 1:
            self.redirect('/error')
        val.append(all_img[0])
        all_img = data.getimages('body-'+name, 'body')
        val.append(all_img)
        soma_part = dict(zip(key, val))
        self.render('soma-part.html', soma_part=soma_part, back_url='/soma')


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        #hotcats = data.gethotcats()
        self.render('index.html')



if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        "debug": True,
        "template_path": os.path.join(os.path.dirname(__file__), "template"),
        "static_path": os.path.join(os.path.dirname(__file__), "static")
        }
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler), (r"/soma", SomaHandler),
            (r"/soma/(\w+)", SomaPartHandler), (r'/book', BookHandler),
            (r"/book/(\w+)", BookPartHandler), (r'.*', ErrorHandler)],
        **settings
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
