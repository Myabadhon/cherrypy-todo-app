import sys
import cherrypy
from mako.template import Template
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://127.0.0.1:8080/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
# app = QApplication(sys.argv)
# QApplication.setApplicationName('TODO')
# window = MainWindow()
# app.exec_()
class Todo(MainWindow):
    @cherrypy.expose
    def index(self):

        mytemplate = Template(filename='template/index.html')
        return mytemplate.render()

    @cherrypy.expose
    def store(self, desc, date):
        return desc

if __name__ == '__main__':
    cherrypy.quickstart(Todo(), '/')
