#!/usr/bin/env python
import os
import time
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class ContactHandler(BaseHandler):
    def get(self):
        return self.render_template("contact.html")

class IndexHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

class LinksHandler(BaseHandler):
    def get(self):
        return self.render_template("links.html")

class PortfolioHandler(BaseHandler):
    def get(self):
        return self.render_template("portfolio.html")

class AboutHandler(BaseHandler):
    def get(self):
        return self.render_template("about.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/contact.html', ContactHandler),
    webapp2.Route('/index.html', IndexHandler),
    webapp2.Route('/links.html', LinksHandler),
    webapp2.Route('/portfolio.html', PortfolioHandler),
    webapp2.Route('/about.html', AboutHandler),
], debug=True)
