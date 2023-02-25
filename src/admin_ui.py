# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qt\admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminMainWindow(object):
    def setupUi(self, AdminMainWindow):
        AdminMainWindow.setObjectName("AdminMainWindow")
        AdminMainWindow.resize(786, 572)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\qt\\../src/resources/aupay-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdminMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AdminMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabUsers = QtWidgets.QWidget()
        self.tabUsers.setObjectName("tabUsers")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tabUsers)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.userSearchLine = QtWidgets.QLineEdit(self.tabUsers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userSearchLine.sizePolicy().hasHeightForWidth())
        self.userSearchLine.setSizePolicy(sizePolicy)
        self.userSearchLine.setObjectName("userSearchLine")
        self.verticalLayout.addWidget(self.userSearchLine)
        self.addUserButton = QtWidgets.QPushButton(self.tabUsers)
        self.addUserButton.setObjectName("addUserButton")
        self.verticalLayout.addWidget(self.addUserButton)
        self.editUserButton = QtWidgets.QPushButton(self.tabUsers)
        self.editUserButton.setObjectName("editUserButton")
        self.verticalLayout.addWidget(self.editUserButton)
        self.deleteUserButton = QtWidgets.QPushButton(self.tabUsers)
        self.deleteUserButton.setObjectName("deleteUserButton")
        self.verticalLayout.addWidget(self.deleteUserButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.usersTable = QtWidgets.QTableWidget(self.tabUsers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usersTable.sizePolicy().hasHeightForWidth())
        self.usersTable.setSizePolicy(sizePolicy)
        self.usersTable.setObjectName("usersTable")
        self.usersTable.setColumnCount(6)
        self.usersTable.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersTable.setItem(0, 5, item)
        self.horizontalLayout_4.addWidget(self.usersTable)
        self.tabWidget.addTab(self.tabUsers, "")
        self.tabTransactions = QtWidgets.QWidget()
        self.tabTransactions.setObjectName("tabTransactions")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tabTransactions)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.transactionSearchButton = QtWidgets.QLineEdit(self.tabTransactions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transactionSearchButton.sizePolicy().hasHeightForWidth())
        self.transactionSearchButton.setSizePolicy(sizePolicy)
        self.transactionSearchButton.setObjectName("transactionSearchButton")
        self.verticalLayout_2.addWidget(self.transactionSearchButton)
        self.addTransactionButton = QtWidgets.QPushButton(self.tabTransactions)
        self.addTransactionButton.setObjectName("addTransactionButton")
        self.verticalLayout_2.addWidget(self.addTransactionButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.transactionsTable = QtWidgets.QTableWidget(self.tabTransactions)
        self.transactionsTable.setObjectName("transactionsTable")
        self.transactionsTable.setColumnCount(6)
        self.transactionsTable.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactionsTable.setItem(0, 5, item)
        self.horizontalLayout_5.addWidget(self.transactionsTable)
        self.tabWidget.addTab(self.tabTransactions, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        AdminMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        self.menubar.setObjectName("menubar")
        AdminMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminMainWindow)
        self.statusbar.setObjectName("statusbar")
        AdminMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminMainWindow)

    def retranslateUi(self, AdminMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminMainWindow.setWindowTitle(_translate("AdminMainWindow", "AUPay Admin"))
        self.userSearchLine.setPlaceholderText(_translate("AdminMainWindow", "Search"))
        self.addUserButton.setText(_translate("AdminMainWindow", "Add User"))
        self.editUserButton.setText(_translate("AdminMainWindow", "Edit User"))
        self.deleteUserButton.setText(_translate("AdminMainWindow", "Delete User"))
        item = self.usersTable.verticalHeaderItem(0)
        item.setText(_translate("AdminMainWindow", "1"))
        item = self.usersTable.verticalHeaderItem(1)
        item.setText(_translate("AdminMainWindow", "2"))
        item = self.usersTable.verticalHeaderItem(2)
        item.setText(_translate("AdminMainWindow", "3"))
        item = self.usersTable.horizontalHeaderItem(0)
        item.setText(_translate("AdminMainWindow", "card_id"))
        item = self.usersTable.horizontalHeaderItem(1)
        item.setText(_translate("AdminMainWindow", "school_id"))
        item = self.usersTable.horizontalHeaderItem(2)
        item.setText(_translate("AdminMainWindow", "password"))
        item = self.usersTable.horizontalHeaderItem(3)
        item.setText(_translate("AdminMainWindow", "otp_key"))
        item = self.usersTable.horizontalHeaderItem(4)
        item.setText(_translate("AdminMainWindow", "user_type"))
        item = self.usersTable.horizontalHeaderItem(5)
        item.setText(_translate("AdminMainWindow", "balance"))
        __sortingEnabled = self.usersTable.isSortingEnabled()
        self.usersTable.setSortingEnabled(False)
        item = self.usersTable.item(0, 0)
        item.setText(_translate("AdminMainWindow", "63cbf5e5947050d54c2ce880"))
        item = self.usersTable.item(0, 1)
        item.setText(_translate("AdminMainWindow", "2052522"))
        item = self.usersTable.item(0, 2)
        item.setText(_translate("AdminMainWindow", "~@FV7HMg++Aq[4&H/}."))
        item = self.usersTable.item(0, 3)
        item.setText(_translate("AdminMainWindow", "sJuoYtp%|-+YgQcjdyb"))
        item = self.usersTable.item(0, 4)
        item.setText(_translate("AdminMainWindow", "student"))
        item = self.usersTable.item(0, 5)
        item.setText(_translate("AdminMainWindow", "12403.00"))
        self.usersTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUsers), _translate("AdminMainWindow", "Users"))
        self.transactionSearchButton.setPlaceholderText(_translate("AdminMainWindow", "Search"))
        self.addTransactionButton.setText(_translate("AdminMainWindow", "Add Transaction"))
        item = self.transactionsTable.verticalHeaderItem(0)
        item.setText(_translate("AdminMainWindow", "1"))
        item = self.transactionsTable.verticalHeaderItem(1)
        item.setText(_translate("AdminMainWindow", "2"))
        item = self.transactionsTable.verticalHeaderItem(2)
        item.setText(_translate("AdminMainWindow", "3"))
        item = self.transactionsTable.horizontalHeaderItem(0)
        item.setText(_translate("AdminMainWindow", "_id"))
        item = self.transactionsTable.horizontalHeaderItem(1)
        item.setText(_translate("AdminMainWindow", "timestamp"))
        item = self.transactionsTable.horizontalHeaderItem(2)
        item.setText(_translate("AdminMainWindow", "source_id"))
        item = self.transactionsTable.horizontalHeaderItem(3)
        item.setText(_translate("AdminMainWindow", "destination_id"))
        item = self.transactionsTable.horizontalHeaderItem(4)
        item.setText(_translate("AdminMainWindow", "amount"))
        item = self.transactionsTable.horizontalHeaderItem(5)
        item.setText(_translate("AdminMainWindow", "description"))
        __sortingEnabled = self.transactionsTable.isSortingEnabled()
        self.transactionsTable.setSortingEnabled(False)
        item = self.transactionsTable.item(0, 0)
        item.setText(_translate("AdminMainWindow", "63cbf5e5947050d54c2ce880"))
        item = self.transactionsTable.item(0, 1)
        item.setText(_translate("AdminMainWindow", "1651363200"))
        item = self.transactionsTable.item(0, 2)
        item.setText(_translate("AdminMainWindow", "2052522"))
        item = self.transactionsTable.item(0, 3)
        item.setText(_translate("AdminMainWindow", "CAFETERIA"))
        item = self.transactionsTable.item(0, 4)
        item.setText(_translate("AdminMainWindow", "65"))
        item = self.transactionsTable.item(0, 5)
        item.setText(_translate("AdminMainWindow", "burger"))
        self.transactionsTable.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTransactions), _translate("AdminMainWindow", "Transactions"))
