import sys

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

# Приветствие тут





class Help:
    "Клас допомоги, пояснення застосунку"
    def help(self, event):
        self.ui.photomenu.setPixmap(QtGui.QPixmap('help 1366.jpg'))
        self.ui.Yellow.clicked.connect(self.yellow)
        self.ui.Blue.clicked.connect(self.blue)
        self.ui.Red.clicked.connect(self.red)
        self.ui.Yellow.show()
        self.ui.Blue.show()
        self.ui.Red.show()
        self.ui.Return.mousePressEvent = self.menu
        self.ui.Return.show()





class Colors:
    "Клас кольорів та дочірні класи, які належать цьому класу"
    def yellow(self, event):
        self.ui.photomenu.setPixmap(QtGui.QPixmap('yellow 1366.png'))
        self.ui.Yellow.hide()
        self.ui.Blue.hide()
        self.ui.Red.hide()
        self.ui.Return.mousePressEvent = self.menu
        self.ui.Return.show()

    def blue(self, event):
        self.ui.photomenu.setPixmap(QtGui.QPixmap('Blue-1366.png'))
        self.ui.Yellow.hide()
        self.ui.Blue.hide()
        self.ui.Red.hide()
        self.ui.Return.mousePressEvent = self.menu
        self.ui.Return.show()

    def red(self, event):
        self.ui.photomenu.setPixmap(QtGui.QPixmap('red 1366.png'))
        self.ui.Yellow.hide()
        self.ui.Blue.hide()
        self.ui.Red.hide()
        self.ui.Return.mousePressEvent = self.menu
        self.ui.Return.show()





class Menu(Colors, Help):
    "Клас головного вікна(меню) та дочірні класи головного вікна(меню)"
    def menu(self, event):
        self.ui.photomenu.setPixmap(QtGui.QPixmap('photo menu.jpg'))
        self.ui.Yellow.clicked.connect(self.yellow)
        self.ui.Blue.clicked.connect(self.blue)
        self.ui.Red.clicked.connect(self.red)
        self.ui.Help.clicked.connect(self.help)
        self.ui.Yellow.show()
        self.ui.Blue.show()
        self.ui.Red.show()
        self.ui.Help.show()
        self.ui.Return.hide()
        self.ui.Start.hide()





class Start(Menu):
    "Початок, вхід до нашої програми"
    def __init__(self):
        self.ui = uic.loadUi('Menu.ui')
        self.ui.photomenu.setPixmap(QtGui.QPixmap('background.jpg'))
        self.ui.Start.clicked.connect(self.menu)
        self.ui.Yellow.hide()
        self.ui.Blue.hide()
        self.ui.Red.hide()
        self.ui.Help.hide()
        self.ui.Return.hide()
        self.ui.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Start()
    sys.exit(app.exec_())
