
from PyQt5 import QtCore, QtGui, QtWidgets
from uyari import Ui_uyari



class Ui_boyolcer( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def uyariac(self):
        santim = self.boygir.text()
        self.ui = Ui_uyari(santim)
        self.ui.show()
        print(santim)

    def setupUi(self):

        self.setObjectName("boyolcer")
        self.resize(370, 159)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.boygir = QtWidgets.QLineEdit(self.centralwidget)
        self.boygir.setGeometry(QtCore.QRect(200, 59, 113, 21))
        self.boygir.setObjectName("boygir")



        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(290, 130, 75, 23))
        self.ok.setObjectName("ok")
        self.setCentralWidget(self.centralwidget)

        self.ok.clicked.connect(self.uyariac)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("boyolcer", "Dijital boy ölçme aleti"))
        self.label.setText(_translate("boyolcer", "Boyunu gir :"))
        self.label_2.setText(_translate("boyolcer", "cm"))
        self.ok.setText(_translate("boyolcer", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_boyolcer()
    ui.show()
    sys.exit(app.exec_())