# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.23.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import imagemTeste_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(228, 222, 255);")
        self.TELADELOGIN = QFrame(self.centralwidget)
        self.TELADELOGIN.setObjectName(u"TELADELOGIN")
        self.TELADELOGIN.setGeometry(QRect(100, 90, 661, 431))
        self.TELADELOGIN.setFrameShape(QFrame.Shape.StyledPanel)
        self.TELADELOGIN.setFrameShadow(QFrame.Shadow.Raised)
        self.usuario = QFrame(self.TELADELOGIN)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setGeometry(QRect(70, 130, 491, 51))
        self.usuario.setFrameShape(QFrame.Shape.StyledPanel)
        self.usuario.setFrameShadow(QFrame.Shadow.Raised)
        self.DADOSUSO = QLineEdit(self.usuario)
        self.DADOSUSO.setObjectName(u"DADOSUSO")
        self.DADOSUSO.setGeometry(QRect(80, 10, 401, 31))
        self.Usuario = QLabel(self.usuario)
        self.Usuario.setObjectName(u"Usuario")
        self.Usuario.setGeometry(QRect(20, 20, 49, 16))
        self.Usuario.setStyleSheet(u"border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));")
        self.senha = QFrame(self.TELADELOGIN)
        self.senha.setObjectName(u"senha")
        self.senha.setGeometry(QRect(70, 220, 491, 51))
        self.senha.setFrameShape(QFrame.Shape.StyledPanel)
        self.senha.setFrameShadow(QFrame.Shadow.Raised)
        self.DADOSSENHA = QLineEdit(self.senha)
        self.DADOSSENHA.setObjectName(u"DADOSSENHA")
        self.DADOSSENHA.setGeometry(QRect(80, 10, 401, 31))
        self.DADOSSENHA.setEchoMode(QLineEdit.EchoMode.Password)
        self.senha_2 = QLabel(self.senha)
        self.senha_2.setObjectName(u"senha_2")
        self.senha_2.setGeometry(QRect(10, 20, 49, 16))
        self.LOGIN = QPushButton(self.TELADELOGIN)
        self.LOGIN.setObjectName(u"LOGIN")
        self.LOGIN.setGeometry(QRect(300, 350, 75, 24))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setBold(True)
        font.setItalic(True)
        self.LOGIN.setFont(font)
        self.lembrar = QCheckBox(self.TELADELOGIN)
        self.lembrar.setObjectName(u"lembrar")
        self.lembrar.setGeometry(QRect(460, 290, 91, 20))
        self.label_2 = QLabel(self.TELADELOGIN)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 60, 90, 16))
        self.label = QLabel(self.TELADELOGIN)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-11, -1, 701, 501))
        self.label.setPixmap(QPixmap(u":/teste/picapau.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.raise_()
        self.usuario.raise_()
        self.senha.raise_()
        self.LOGIN.raise_()
        self.lembrar.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Usuario.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio:", None))
        self.senha_2.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.LOGIN.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.lembrar.setText(QCoreApplication.translate("MainWindow", u"Lembrar-me", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Empresa PicaPau", None))
        self.label.setText("")
    # retranslateUi
if __name__=='_main_':
    import sys
    app= QApplication(sys.argv)
    w= QMainWindow()
    ui= Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    app.exec