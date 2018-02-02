from PyQt5.QtWidgets import  QStyleFactory
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

from PyQt5 import QtGui, QtCore

#from PyQt5.QtWidgets import QDialog, QStyleFactory, QWidget, QFileDialog, QMenu,QInputDialog, QAction, QPushButton, QItemDelegate, QTableWidgetItem, QCheckBox

def setStyle(app):

    app.setStyle(QStyleFactory.create("Fusion"))

    darkPalette = QPalette()
    
    darkPalette.setColor(QPalette.Window, QColor.fromRgb(53,53,53))
    darkPalette.setColor(QPalette.WindowText, Qt.white)
    darkPalette.setColor(QPalette.Base, QColor.fromRgb(25,25,25))
    darkPalette.setColor(QPalette.AlternateBase, QColor.fromRgb(53,53,53))
    darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
    darkPalette.setColor(QPalette.ToolTipText, Qt.white)
    darkPalette.setColor(QPalette.Text, Qt.white)
    darkPalette.setColor(QPalette.Button, QColor.fromRgb(53,53,53))
    darkPalette.setColor(QPalette.ButtonText, Qt.white)
    darkPalette.setColor(QPalette.BrightText, Qt.red)
    darkPalette.setColor(QPalette.Link, QColor.fromRgb(42, 130, 218))

    darkPalette.setColor(QPalette.Highlight, QColor.fromRgb(42, 130, 218))
    darkPalette.setColor(QPalette.HighlightedText, Qt.black)

    app_icon = QtGui.QIcon()
    app_icon.addFile('artwork/icons16.png', QtCore.QSize(16,16))
    app_icon.addFile('artwork/icons24.png', QtCore.QSize(24,24))
    app_icon.addFile('artwork/icons32.png', QtCore.QSize(32,32))
    app_icon.addFile('artwork/icons48.png', QtCore.QSize(48,48))
    app_icon.addFile('artwork/icons256.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)

    app.setPalette(darkPalette)

    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")