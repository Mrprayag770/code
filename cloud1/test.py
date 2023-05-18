import webapp2
import os


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello class, Welcome to Cloud Computing Lab!")


class IndexPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        with open(os.path.join('static', 'index.html'), 'r') as file:
            self.response.write(file.read())


app = webapp2.WSGIApplication([
    ('/', IndexPage)
], debug=True)
