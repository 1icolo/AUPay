# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditUserDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 321)
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setAutoFillBackground(False)
        Dialog.setModal(False)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 60, 271, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cardID_editUser = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cardID_editUser.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cardID_editUser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cardID_editUser.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cardID_editUser.setFrame(True)
        self.cardID_editUser.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.cardID_editUser.setClearButtonEnabled(False)
        self.cardID_editUser.setObjectName("cardID_editUser")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cardID_editUser)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.schoolID_editUser = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.schoolID_editUser.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.schoolID_editUser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.schoolID_editUser.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.schoolID_editUser.setFrame(True)
        self.schoolID_editUser.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.schoolID_editUser.setClearButtonEnabled(False)
        self.schoolID_editUser.setObjectName("schoolID_editUser")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.schoolID_editUser)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_editUser = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_editUser.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password_editUser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.password_editUser.setFrame(True)
        self.password_editUser.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_editUser.setClearButtonEnabled(False)
        self.password_editUser.setObjectName("password_editUser")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_editUser)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.userType_editUser = QtWidgets.QComboBox(self.formLayoutWidget)
        self.userType_editUser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.userType_editUser.setEditable(False)
        self.userType_editUser.setFrame(True)
        self.userType_editUser.setObjectName("userType_editUser")
        self.userType_editUser.addItem("")
        self.userType_editUser.addItem("")
        self.userType_editUser.addItem("")
        self.userType_editUser.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.userType_editUser)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.otpSecret_editUser = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.otpSecret_editUser.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.otpSecret_editUser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.otpSecret_editUser.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.otpSecret_editUser.setFrame(True)
        self.otpSecret_editUser.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.otpSecret_editUser.setReadOnly(True)
        self.otpSecret_editUser.setClearButtonEnabled(False)
        self.otpSecret_editUser.setObjectName("otpSecret_editUser")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.otpSecret_editUser)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.otp_editUser = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.otp_editUser.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.otp_editUser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.otp_editUser.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.otp_editUser.setFrame(True)
        self.otp_editUser.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.otp_editUser.setClearButtonEnabled(False)
        self.otp_editUser.setObjectName("otp_editUser")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.otp_editUser)
        self.buttonGenerate_editUser = QtWidgets.QPushButton(self.formLayoutWidget)
        self.buttonGenerate_editUser.setObjectName("buttonGenerate_editUser")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.buttonGenerate_editUser)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 260, 171, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonSave_editUser = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonSave_editUser.setObjectName("buttonSave_editUser")
        self.horizontalLayout.addWidget(self.buttonSave_editUser)
        self.buttonCancel_editUser = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.buttonCancel_editUser.setObjectName("buttonCancel_editUser")
        self.horizontalLayout.addWidget(self.buttonCancel_editUser)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit User"))
        self.label_5.setText(_translate("Dialog", "Card ID:"))
        self.label.setText(_translate("Dialog", "School ID:"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.label_3.setText(_translate("Dialog", "User Type:"))
        self.userType_editUser.setItemText(0, _translate("Dialog", "User"))
        self.userType_editUser.setItemText(1, _translate("Dialog", "Business"))
        self.userType_editUser.setItemText(2, _translate("Dialog", "Teller"))
        self.userType_editUser.setItemText(3, _translate("Dialog", "Admin"))
        self.label_4.setText(_translate("Dialog", "OTP Secret"))
        self.label_6.setText(_translate("Dialog", "OTP"))
        self.buttonGenerate_editUser.setText(_translate("Dialog", "Generate New Secret"))
        self.buttonSave_editUser.setText(_translate("Dialog", "Save"))
        self.buttonCancel_editUser.setText(_translate("Dialog", "Cancel"))
