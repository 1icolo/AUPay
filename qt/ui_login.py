# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwnypLW.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(217, 173)
        Dialog.setMaximumSize(QSize(325, 302))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.idLine = QLineEdit(self.widget)
        self.idLine.setObjectName(u"idLine")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.idLine)

        self.passwordLine = QLineEdit(self.widget)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setMaxLength(20)
        self.passwordLine.setEchoMode(QLineEdit.Password)
        self.passwordLine.setClearButtonEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.passwordLine)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(3, QFormLayout.SpanningRole, self.verticalSpacer)

        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy1)
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginButton.setMouseTracking(True)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.loginButton)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.idLine.setPlaceholderText(QCoreApplication.translate("Dialog", u"School ID", None))
        self.passwordLine.setInputMask("")
        self.passwordLine.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("Dialog", u"Login", None))
    # retranslateUi

