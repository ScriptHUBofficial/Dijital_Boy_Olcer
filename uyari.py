######################### QT LIB #########################
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_uyari( QtWidgets.QMainWindow ):
    def __init__(self , santim):
        super().__init__()
        self.santim = santim
        self.setupUi()


    def setupUi(self):
        self.setObjectName("uyari")
        self.resize(296, 174)
        self.boysonuc = QtWidgets.QLabel(self)
        self.boysonuc.setGeometry(QtCore.QRect(80, 70, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.boysonuc.setFont(font)
        self.boysonuc.setObjectName("boysonuc")

        self.logo = QtWidgets.QLabel()
        self.logo.setGeometry(QtCore.QRect(20, 70, 47, 41))
        self.logo.setText("")
        self.logo.setObjectName("logo")

        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("uyari", "Uyarı"))
        self.boysonuc.setText(_translate("uyari", "Boyunuz " + self.santim + " cm" ))
