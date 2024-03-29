# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(648, 591)
        Form.setStyleSheet("Form{\n"
"background:transparent;\n"
"}\n"
"\n"
"*{\n"
"font-family: helvetica;\n"
"font-size:15px;\n"
"color:#ff8ff8;\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"background:#404040\n"
"}\n"
"\n"
"QToolButton{\n"
"background: #ff2ff2;\n"
"border-radius: 15px;\n"
"color:#404040;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"background:#ff2ff2;\n"
"color:#ff9ff9;\n"
"font-weight:bold;\n"
"border-radius:15;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"color:#ff2ff2;\n"
"background:#333;\n"
"\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"color:#777777;\n"
"border-bottom:0.5px solid #ff2ff2;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(150, 120, 341, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 60, 91, 51))
        self.label.setStyleSheet("font-family:helvetica;\n"
"font-size:25px;\n"
"font-weight: bold;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(60, 232, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 119, 191, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 170, 191, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(260, 50, 121, 121))
        self.toolButton.setStyleSheet("image: url(:/user2/user2.png);")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "LOGIN"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))

import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

#pyrcc5 source.qrc -o resource_rc.py
