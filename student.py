# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_student(object):
    def setupUi(self, student):
        student.setObjectName("student")
        student.resize(853, 654)
        student.setSizeGripEnabled(True)
        student.setModal(True)
        self.gridLayout_3 = QtWidgets.QGridLayout(student)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(student)
        self.tabWidget.setObjectName("tabWidget")
        self.information_tab = QtWidgets.QWidget()
        self.information_tab.setObjectName("information_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.information_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.information_tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(12, 116, 45, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(12, 236, 45, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(12, 356, 45, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(71, 116, 171, 24))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 236, 171, 24))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(71, 356, 171, 24))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(12, 476, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.information_tab)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(12, 147, 30, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(12, 298, 30, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(12, 449, 45, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(64, 298, 171, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(64, 147, 171, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(64, 449, 171, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.information_tab, "")
        self.collection_tab = QtWidgets.QWidget()
        self.collection_tab.setObjectName("collection_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.collection_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.collection_tab)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 4, item)
        self.gridLayout_4.addWidget(self.tableWidget_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.collection_tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.collection_tab, "")
        self.menu_tab = QtWidgets.QWidget()
        self.menu_tab.setObjectName("menu_tab")
        self.tableWidget = QtWidgets.QTableWidget(self.menu_tab)
        self.tableWidget.setGeometry(QtCore.QRect(11, 223, 811, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.menu_tab)
        self.tableWidget_4.setGeometry(QtCore.QRect(11, 11, 811, 111))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 4, item)
        self.pushButton = QtWidgets.QPushButton(self.menu_tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 811, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.menu_tab)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 180, 811, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.menu_tab, "")
        self.function_tab = QtWidgets.QWidget()
        self.function_tab.setObjectName("function_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.function_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.function_tab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, item)
        self.gridLayout_6.addWidget(self.tableWidget_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_6.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.function_tab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(student)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(student)

    def retranslateUi(self, student):
        _translate = QtCore.QCoreApplication.translate
        student.setWindowTitle(_translate("student", "Dialog"))
        self.groupBox_2.setTitle(_translate("student", "修改密码"))
        self.label_4.setText(_translate("student", "旧密码"))
        self.label_5.setText(_translate("student", "新密码"))
        self.label_6.setText(_translate("student", "新密码"))
        self.pushButton_5.setText(_translate("student", "确定修改"))
        self.groupBox.setTitle(_translate("student", "基本信息"))
        self.label.setText(_translate("student", "学号"))
        self.label_2.setText(_translate("student", "姓名"))
        self.label_3.setText(_translate("student", "收藏数"))
        self.lineEdit_2.setText(_translate("student", "2"))
        self.lineEdit.setText(_translate("student", "1"))
        self.lineEdit_3.setText(_translate("student", "3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.information_tab), _translate("student", "个人信息"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("student", "序号"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("student", "1"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("student", "2"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("student", "3"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("student", "4"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("student", "5"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("student", "6"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("student", "7"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("student", "8"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("student", "9"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("student", "10"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("student", "饭菜名"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("student", "窗口号"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("student", "价格"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("student", "窗口名"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("student", "状态"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("student", "     （单价/元）"))
        item = self.tableWidget_2.item(0, 4)
        item.setText(_translate("student", "（在售/已下架）"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("student", "取消收藏"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.collection_tab), _translate("student", "我的收藏"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("student", "序号"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("student", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("student", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("student", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("student", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("student", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("student", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("student", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("student", "8"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("student", "9"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("student", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("student", "饭菜名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("student", "窗口号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("student", "价格"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("student", "窗口名"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("student", "状态"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("student", "      （单位/元）"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("student", "（在售/已下架）"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("student", "序号"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("student", "0"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("student", "饭菜名"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("student", "窗口号"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("student", "价格"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("student", "窗口名"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("student", "状态"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        item = self.tableWidget_4.item(0, 2)
        item.setText(_translate("student", "    （单价/元）"))
        item = self.tableWidget_4.item(0, 4)
        item.setText(_translate("student", "（在售/已下架）"))
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("student", "查询"))
        self.pushButton_2.setText(_translate("student", "收藏"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.menu_tab), _translate("student", "菜单"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("student", "饭菜名"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("student", "窗口号"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("student", "价格"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("student", "窗口名"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("student", "状态"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 2)
        item.setText(_translate("student", "     （单价/元）"))
        item = self.tableWidget_3.item(0, 4)
        item.setText(_translate("student", "（在售/已下架）"))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("student", "随机选餐"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("student", "随机选餐"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("student", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.function_tab), _translate("student", "功能"))