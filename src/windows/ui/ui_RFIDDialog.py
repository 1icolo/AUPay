# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Nico\AUPay\src\windows\ui\RFIDDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RFIDDialog(object):
    def setupUi(self, RFIDDialog):
        RFIDDialog.setObjectName("RFIDDialog")
        RFIDDialog.resize(263, 149)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RFIDDialog.sizePolicy().hasHeightForWidth())
        RFIDDialog.setSizePolicy(sizePolicy)
        RFIDDialog.setMinimumSize(QtCore.QSize(263, 149))
        RFIDDialog.setMaximumSize(QtCore.QSize(263, 149))
        RFIDDialog.setToolTipDuration(2)
        RFIDDialog.setAutoFillBackground(True)
        self.gridLayout = QtWidgets.QGridLayout(RFIDDialog)
        self.gridLayout.setContentsMargins(20, 29, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.seconds = QtWidgets.QLabel(RFIDDialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.seconds.setFont(font)
        self.seconds.setText("")
        self.seconds.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.seconds.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.seconds.setObjectName("seconds")
        self.gridLayout.addWidget(self.seconds, 1, 0, 1, 1)
        self.message = QtWidgets.QLabel(RFIDDialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.message.setFont(font)
        self.message.setTextFormat(QtCore.Qt.AutoText)
        self.message.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.message.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.message.setObjectName("message")
        self.gridLayout.addWidget(self.message, 0, 0, 1, 1)

        self.retranslateUi(RFIDDialog)
        QtCore.QMetaObject.connectSlotsByName(RFIDDialog)

    def retranslateUi(self, RFIDDialog):
        _translate = QtCore.QCoreApplication.translate
        RFIDDialog.setWindowTitle(_translate("RFIDDialog", "RFID"))
        RFIDDialog.setToolTip(_translate("RFIDDialog", "bro"))
        self.message.setText(_translate("RFIDDialog", "RFID detected"))
