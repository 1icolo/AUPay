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
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(369, 446)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.scroll_area_item_list = QtWidgets.QScrollArea(Dialog)
        self.scroll_area_item_list.setWidgetResizable(True)
        self.scroll_area_item_list.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scroll_area_item_list.setObjectName("scroll_area_item_list")
        self.scroll_area_container = QtWidgets.QWidget()
        self.scroll_area_container.setGeometry(QtCore.QRect(0, 0, 349, 204))
        self.scroll_area_container.setObjectName("scroll_area_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scroll_area_container)
        self.verticalLayout.setObjectName("verticalLayout")
        self.form_layout_item_list = QtWidgets.QFormLayout()
        self.form_layout_item_list.setObjectName("form_layout_item_list")
        self.verticalLayout.addLayout(self.form_layout_item_list)
        self.scroll_area_item_list.setWidget(self.scroll_area_container)
        self.gridLayout.addWidget(self.scroll_area_item_list, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.amountLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.amountLabel.setFont(font)
        self.amountLabel.setObjectName("amountLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.amountLabel)
        self.amountLineEdit = QtWidgets.QDoubleSpinBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.amountLineEdit.setFont(font)
        self.amountLineEdit.setReadOnly(True)
        self.amountLineEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.amountLineEdit.setMaximum(100000.0)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.amountLineEdit)
        self.buttonScanBusiness = QtWidgets.QPushButton(Dialog)
        self.buttonScanBusiness.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.buttonScanBusiness.setFont(font)
        self.buttonScanBusiness.setCheckable(False)
        self.buttonScanBusiness.setChecked(False)
        self.buttonScanBusiness.setObjectName("buttonScanBusiness")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.buttonScanBusiness)
        self.buttonScanUser = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.buttonScanUser.setFont(font)
        self.buttonScanUser.setObjectName("buttonScanUser")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.buttonScanUser)
        self.gridLayout.addLayout(self.formLayout, 6, 0, 1, 1)
        self.buttonSave_addTransaction = QtWidgets.QPushButton(Dialog)
        self.buttonSave_addTransaction.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.buttonSave_addTransaction.setFont(font)
        self.buttonSave_addTransaction.setObjectName("buttonSave_addTransaction")
        self.gridLayout.addWidget(self.buttonSave_addTransaction, 8, 0, 1, 1)
        self.line_item_list = QtWidgets.QFrame(Dialog)
        self.line_item_list.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_item_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_item_list.setObjectName("line_item_list")
        self.gridLayout.addWidget(self.line_item_list, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.label_quantity = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_quantity.sizePolicy().hasHeightForWidth())
        self.label_quantity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_quantity.setFont(font)
        self.label_quantity.setObjectName("label_quantity")
        self.horizontalLayout.addWidget(self.label_quantity)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Chargeback"))
        self.amountLabel.setText(_translate("Dialog", "Amount:"))
        self.buttonScanBusiness.setText(_translate("Dialog", "Verify Business"))
        self.buttonScanUser.setText(_translate("Dialog", "Verify User"))
        self.buttonSave_addTransaction.setText(_translate("Dialog", "Chargeback"))
        self.label_name.setText(_translate("Dialog", "Name"))
        self.label_quantity.setText(_translate("Dialog", "Quantity"))
