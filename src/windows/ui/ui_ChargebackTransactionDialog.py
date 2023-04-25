# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Nico\AUPay\src\windows\ui\ChargebackTransactionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(516, 339)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.sourceIDLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.sourceIDLabel.setFont(font)
        self.sourceIDLabel.setObjectName("sourceIDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.sourceIDLabel)
        self.sourceIDLineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.sourceIDLineEdit.setFont(font)
        self.sourceIDLineEdit.setReadOnly(True)
        self.sourceIDLineEdit.setObjectName("sourceIDLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sourceIDLineEdit)
        self.destinationIDLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.destinationIDLabel.setFont(font)
        self.destinationIDLabel.setObjectName("destinationIDLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.destinationIDLabel)
        self.destinationIDLineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.destinationIDLineEdit.setFont(font)
        self.destinationIDLineEdit.setReadOnly(True)
        self.destinationIDLineEdit.setObjectName("destinationIDLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.destinationIDLineEdit)
        self.amountLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.amountLabel.setFont(font)
        self.amountLabel.setObjectName("amountLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.amountLabel)
        self.amountLineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.amountLineEdit.setFont(font)
        self.amountLineEdit.setReadOnly(False)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.amountLineEdit)
        self.descriptionLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.descriptionLabel)
        self.descriptionLineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.descriptionLineEdit.setFont(font)
        self.descriptionLineEdit.setReadOnly(True)
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.descriptionLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonSave_addTransaction = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.buttonSave_addTransaction.setFont(font)
        self.buttonSave_addTransaction.setObjectName("buttonSave_addTransaction")
        self.horizontalLayout_2.addWidget(self.buttonSave_addTransaction)
        self.buttonCancel_addTransaction = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.buttonCancel_addTransaction.setFont(font)
        self.buttonCancel_addTransaction.setObjectName("buttonCancel_addTransaction")
        self.horizontalLayout_2.addWidget(self.buttonCancel_addTransaction)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 1, 1, 3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkBoxBusiness = QtWidgets.QCheckBox(Dialog)
        self.checkBoxBusiness.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.checkBoxBusiness.setFont(font)
        self.checkBoxBusiness.setCheckable(True)
        self.checkBoxBusiness.setChecked(False)
        self.checkBoxBusiness.setTristate(False)
        self.checkBoxBusiness.setObjectName("checkBoxBusiness")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBoxBusiness)
        self.buttonScanBusiness = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.buttonScanBusiness.setFont(font)
        self.buttonScanBusiness.setCheckable(False)
        self.buttonScanBusiness.setObjectName("buttonScanBusiness")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.buttonScanBusiness)
        self.checkBoxUser = QtWidgets.QCheckBox(Dialog)
        self.checkBoxUser.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.checkBoxUser.setFont(font)
        self.checkBoxUser.setCheckable(True)
        self.checkBoxUser.setChecked(False)
        self.checkBoxUser.setTristate(False)
        self.checkBoxUser.setObjectName("checkBoxUser")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBoxUser)
        self.buttonScanUser = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.buttonScanUser.setFont(font)
        self.buttonScanUser.setObjectName("buttonScanUser")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.buttonScanUser)
        self.gridLayout.addLayout(self.formLayout_2, 3, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Transaction"))
        self.sourceIDLabel.setText(_translate("Dialog", "Source ID:"))
        self.destinationIDLabel.setText(_translate("Dialog", "Destination ID:"))
        self.amountLabel.setText(_translate("Dialog", "Amount:"))
        self.descriptionLabel.setText(_translate("Dialog", "Description: "))
        self.buttonSave_addTransaction.setText(_translate("Dialog", "Save"))
        self.buttonCancel_addTransaction.setText(_translate("Dialog", "Cancel"))
        self.checkBoxBusiness.setText(_translate("Dialog", "Business"))
        self.buttonScanBusiness.setText(_translate("Dialog", "Scan ID"))
        self.checkBoxUser.setText(_translate("Dialog", "User"))
        self.buttonScanUser.setText(_translate("Dialog", "Scan ID"))
