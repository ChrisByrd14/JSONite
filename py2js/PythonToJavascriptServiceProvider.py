from masonite.provider import ServiceProvider

from .PythonToJavascript import PythonToJavascript

class Py2JsServiceProvider(ServiceProvider):
    ''' Bind Py2Js class into the Service Container '''

    wsgi = True

    def boot(self):
        pass

    def register(self):
        self.app.bind('PythonToJavascript', PythonToJavascript)
