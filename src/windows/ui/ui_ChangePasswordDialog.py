# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Nico\AUPay\src\windows\ui\ChangePasswordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(425, 410)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.line_old_password = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.line_old_password.setFont(font)
        self.line_old_password.setMaxLength(50)
        self.line_old_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.line_old_password.setObjectName("line_old_password")
        self.verticalLayout.addWidget(self.line_old_password)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.line_new_password = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.line_new_password.setFont(font)
        self.line_new_password.setMaxLength(50)
        self.line_new_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.line_new_password.setObjectName("line_new_password")
        self.verticalLayout.addWidget(self.line_new_password)
        self.line_confirm_password = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.line_confirm_password.setFont(font)
        self.line_confirm_password.setMaxLength(50)
        self.line_confirm_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.line_confirm_password.setObjectName("line_confirm_password")
        self.verticalLayout.addWidget(self.line_confirm_password)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.button_change_password = QtWidgets.QPushButton(Dialog)
        self.button_change_password.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.button_change_password.setFont(font)
        self.button_change_password.setObjectName("button_change_password")
        self.verticalLayout.addWidget(self.button_change_password)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Change Password"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password must be at least: </span></p><p><span style=\" font-family:\'Symbol\'; font-size:12pt;\">· </span><span style=\" font-size:12pt;\">at least 8 characters long (12345678)</span></p><p><span style=\" font-family:\'Symbol\'; font-size:12pt;\">· </span><span style=\" font-size:12pt;\">contains both an uppercase and lowercase character (Aa)</span></p><p><span style=\" font-family:\'Symbol\'; font-size:12pt;\">· </span><span style=\" font-size:12pt;\">contains a non-alphanumerical character (!@#$%^&amp;*()_)</span></p><p><span style=\" font-size:12pt; font-weight:600;\">Example:</span><span style=\" font-size:12pt;\"> AUPbsit#2023</span></p></body></html>"))
        self.line_old_password.setPlaceholderText(_translate("Dialog", "Old Password"))
        self.line_new_password.setPlaceholderText(_translate("Dialog", "New Password"))
        self.line_confirm_password.setPlaceholderText(_translate("Dialog", "Confirm Password"))
        self.button_change_password.setToolTip(_translate("Dialog", "If this button is disabled, you probably didn\'t complete the password requirements."))
        self.button_change_password.setText(_translate("Dialog", "Change Password"))
