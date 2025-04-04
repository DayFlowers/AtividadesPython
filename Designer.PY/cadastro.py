# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(532, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CADASTRO = QFrame(self.centralwidget)
        self.CADASTRO.setObjectName(u"CADASTRO")
        self.CADASTRO.setGeometry(QRect(20, 60, 421, 531))
        self.CADASTRO.setFrameShape(QFrame.Shape.StyledPanel)
        self.CADASTRO.setFrameShadow(QFrame.Shadow.Raised)
        self.NomeColaborador = QFrame(self.CADASTRO)
        self.NomeColaborador.setObjectName(u"NomeColaborador")
        self.NomeColaborador.setGeometry(QRect(0, 110, 411, 51))
        self.NomeColaborador.setFrameShape(QFrame.Shape.StyledPanel)
        self.NomeColaborador.setFrameShadow(QFrame.Shadow.Raised)
        self.dadosnome = QLineEdit(self.NomeColaborador)
        self.dadosnome.setObjectName(u"dadosnome")
        self.dadosnome.setGeometry(QRect(80, 10, 311, 31))
        self.Nome_2 = QLabel(self.NomeColaborador)
        self.Nome_2.setObjectName(u"Nome_2")
        self.Nome_2.setGeometry(QRect(10, 20, 49, 16))
        self.senhacolaborador = QFrame(self.CADASTRO)
        self.senhacolaborador.setObjectName(u"senhacolaborador")
        self.senhacolaborador.setGeometry(QRect(0, 170, 411, 41))
        self.senhacolaborador.setFrameShape(QFrame.Shape.StyledPanel)
        self.senhacolaborador.setFrameShadow(QFrame.Shadow.Raised)
        self.dadosemail = QLineEdit(self.senhacolaborador)
        self.dadosemail.setObjectName(u"dadosemail")
        self.dadosemail.setGeometry(QRect(80, 0, 311, 31))
        self.dadosemail.setEchoMode(QLineEdit.EchoMode.Password)
        self.senha_colaborador = QLabel(self.senhacolaborador)
        self.senha_colaborador.setObjectName(u"senha_colaborador")
        self.senha_colaborador.setGeometry(QRect(10, 10, 49, 16))
        self.CadastroCliente = QLabel(self.CADASTRO)
        self.CadastroCliente.setObjectName(u"CadastroCliente")
        self.CadastroCliente.setGeometry(QRect(180, 10, 121, 51))
        self.Cadastrar = QPushButton(self.CADASTRO)
        self.Cadastrar.setObjectName(u"Cadastrar")
        self.Cadastrar.setGeometry(QRect(190, 350, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 532, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Nome_2.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.senha_colaborador.setText(QCoreApplication.translate("MainWindow", u"senha:", None))
        self.CadastroCliente.setText(QCoreApplication.translate("MainWindow", u"Cadastro Colaborador", None))
        self.Cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())