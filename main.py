from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sql
import user
from login import Ui_login as login
from logon import  Ui_logon as logon
from student import Ui_student as student
from admin import Ui_admin as admin

class Login(QMainWindow,login):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.lineEdit.setPlaceholderText("Please enter your username")
        self.lineEdit_2.setPlaceholderText("Please enter your password")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)#密码显示为黑点
        self.pushButton.clicked.connect(self.student_login)
        self.pushButton_2.clicked.connect(self.admin_login)
        self.pushButton_3.clicked.connect(self.student_logon)

    def student_login(self):
        try:
            username = None
            password = None

            username=self.lineEdit.text()
            user.current_student=username
            results=sql.do("select password from student where sno='%s'" % (username))
            (password,)=results[0]

            if self.lineEdit_2.text() == password:
                self.window2=Student()
                self.close()
                self.window2.show()
            else:
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                QMessageBox.information(self,"information","学号或密码错误！")
        except:
            pass

    def admin_login(self):
        try:
            username = None
            password = None

            username=self.lineEdit.text()
            user.current_admin=username
            results=sql.do("select password from admin where ano='%s'" % (username))
            (password,)=results[0]

            if self.lineEdit_2.text() == password:
                self.window4 = Admin()
                self.close()
                self.window4.show()
            else:
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                QMessageBox.information(self, "information", "工号或密码错误！")
        except:
            pass

    def student_logon(self):
        self.window3=Logon()
        self.window3.show()

class Logon(QDialog,logon):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)  # 密码显示为黑点
        self.lineEdit_3.setEchoMode(QLineEdit.Password)  # 密码显示为黑点
        self.pushButton.clicked.connect(self.register)

    def register(self):
        try:
            sno=self.lineEdit.text()
            sname=self.lineEdit_4.text()
            password1=self.lineEdit_2.text()
            password2=self.lineEdit_3.text()

            if len(sno)==0:
                QMessageBox.information(self,"information","请输入学号！")
            else:
                results=sql.do("select * from student where sno=%s" % sno)
                if len(results)==0:
                    if password1==password2:
                        sql.do("insert into student values(%s,'%s','%s')" % (sno,sname,password1))
                        QMessageBox.information(self,"information","注册成功，请登录！")
                    else:
                        QMessageBox.information(self,"information","两次密码不同，请确认！")
                else:
                    QMessageBox.information(self,"information","该学号已注册！")
        except:
            pass


class Student(QDialog,student):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show_information()
        self.show_collection()
        self.show_menu()

        self.lineEdit_4.setEchoMode(QLineEdit.Password)  # 密码显示为黑点
        self.lineEdit_5.setEchoMode(QLineEdit.Password)  # 密码显示为黑点
        self.lineEdit_6.setEchoMode(QLineEdit.Password)  # 密码显示为黑点

        self.pushButton_5.clicked.connect(self.change_password)
        self.pushButton.clicked.connect(self.search_food)
        self.pushButton_2.clicked.connect(self.collection)
        self.pushButton_3.clicked.connect(self.cancel_collection)
        self.pushButton_4.clicked.connect(self.random_food)


    def show_information(self):
        results=sql.do("select * from student where sno=%s" % user.current_student)
        sno=str(results[0][0])
        sname=str(results[0][1])
        results=sql.do("select count(*) from collection where sno=%s" % user.current_student)
        cnum=str(results[0][0])

        self.lineEdit.setText(sno)
        self.lineEdit_2.setText(sname)
        self.lineEdit_3.setText(cnum)


    def show_collection(self):
        results = sql.do("select food.fname,food.wno,food.price,windows.wname,food.state"
                         " from collection,food,windows"
                         " where collection.sno=%s"
                         " and food.wno=windows.wno"
                         " and collection.fname=food.fname" % (user.current_student))

        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(len(results) + 1)

        for i in range(len(results)):
            self.tableWidget_2.setVerticalHeaderItem(i + 1, QTableWidgetItem(str(i + 1)))
        for i in range(len(results)):
            for j in range(len(results[i])):
                self.tableWidget_2.setItem(i + 1, j, QTableWidgetItem(str(results[i][j])))

    def show_menu(self):
        results=sql.do("select * from menu")
        #菜单列表
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(results)+1)

        for i in range(len(results)):
            self.tableWidget.setVerticalHeaderItem(i+1,QTableWidgetItem(str(i+1)))
        for i in range(len(results)):
            for j in range(len(results[i])):
                self.tableWidget.setItem(i+1,j,QTableWidgetItem(str(results[i][j])))

        #搜索列表
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(2)

        for i in range(5):
            self.tableWidget_4.setItem(1,i,QTableWidgetItem(''))

    def show_function(self):
        pass

    def change_password(self):
        old_password=self.lineEdit_4.text()
        new_password=self.lineEdit_5.text()
        new_password_1=self.lineEdit_6.text()

        if len(old_password)==0:
            QMessageBox.information(self,"information","请输入旧密码！")
        else:
            results=sql.do("select password from student where sno=%s" % user.current_student)
            now_password=str(results[0][0])
            if now_password==old_password:
                if len(new_password)!=0:
                    if new_password_1!=new_password:
                        QMessageBox.information(self,"information","两次密码不同，请确认！")
                    else:
                        sql.do("update student set password='%s' where sno=%s" % (new_password,user.current_student))
                        QMessageBox.information(self,"information","修改成功！")
                else:
                    QMessageBox.information(self,"information","新密码不能为空，请输入！")
            else:
                QMessageBox.information(self,"information","旧密码错误，请重新输入！")

    def cancel_collection(self):
        try:
            current_food=self.tableWidget_2.item(self.tableWidget_2.currentRow(),0).text()
            sql.do("delete from collection where fname='%s'" % (current_food))
            QMessageBox.information(self,"information","取消收藏%s成功！" % (current_food))
            self.show_collection()
        except:
            pass


    def collection(self):
        try:
            current_food=self.tableWidget.item(self.tableWidget.currentRow(),0).text()
            if len(current_food)!=0:
                results=sql.do("select * from collection where fname='%s' and sno=%s" % (current_food,user.current_student))
                if len(results)==0:
                    sql.do("insert into collection values(%s,'%s')" % (user.current_student,current_food))
                    QMessageBox.information(self,"information","收藏%s成功!" %(current_food))
                    self.show_collection()
                    self.show_information()
                else:
                    QMessageBox.information(self,"information","%s已收藏,请勿重复收藏!" %(current_food))
        except:
            pass

    def search_food(self):
        fname=self.tableWidget_4.item(1,0).text()
        wno=self.tableWidget_4.item(1,1).text()
        price=self.tableWidget_4.item(1,2).text()
        wname=self.tableWidget_4.item(1,3).text()
        state=self.tableWidget_4.item(1,4).text()

        #动态生成sql查询语句
        search_sql="select * from menu where " \
                   "(fname like '%{0}%' or '{0}'='') " \
                   "and (wno='{1}' or '{1}'='') " \
                   "and (price='{2}' or '{2}'='') " \
                   "and (wname='{3}' or '{3}'='') " \
                   "and (state='{4}' or '{4}'='')".format(fname,wno,price,wname,state)

        results=sql.do(search_sql)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(len(results) + 1)

        for i in range(len(results)):
            self.tableWidget.setVerticalHeaderItem(i + 1, QTableWidgetItem(str(i + 1)))
        for i in range(len(results)):
            for j in range(len(results[i])):
                self.tableWidget.setItem(i + 1, j, QTableWidgetItem(str(results[i][j])))


    def random_food(self):
        try:
            results=sql.do("select * from menu where state='在售'")
            random_one=random.choice(results)
            self.tableWidget_3.setColumnCount(5)
            self.tableWidget_3.setRowCount(2)
            for i in range(5):
                self.tableWidget_3.setItem(1, i, QTableWidgetItem(str(random_one[i])))
        except:
            pass


class Admin(QDialog,admin):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show_information()
        self.show_menu()

        self.lineEdit_2.setEchoMode(QLineEdit.Password)  # 密码显示为黑点
        self.lineEdit_3.setEchoMode(QLineEdit.Password)  # 密码显示为黑点
        self.lineEdit_4.setEchoMode(QLineEdit.Password)  # 密码显示为黑点

        self.pushButton_5.clicked.connect(self.change_password)
        self.pushButton.clicked.connect(self.change_food)
        self.pushButton_3.clicked.connect(self.add_food)
        self.pushButton_2.clicked.connect(self.change_state)
        self.pushButton_4.clicked.connect(self.search_food)
        self.pushButton_6.clicked.connect(self.delete_food)
        self.pushButton_7.clicked.connect(self.change_wname)

    def show_information(self):
        self.lineEdit.setText(str(user.current_admin))

    def show_menu(self):
        results=sql.do("select * from menu")

        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(len(results)+1)

        for i in range(len(results)):
            self.tableWidget_2.setVerticalHeaderItem(i+1,QTableWidgetItem(str(i+1)))
        for i in range(len(results)):
            for j in range(len(results[i])):
                self.tableWidget_2.setItem(i+1,j,QTableWidgetItem(str(results[i][j])))

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(2)

        for i in range(5):
            self.tableWidget.setItem(1, i, QTableWidgetItem(''))


    def change_password(self):
        old_password = self.lineEdit_2.text()
        new_password = self.lineEdit_3.text()
        new_password_1 = self.lineEdit_4.text()

        if len(old_password) == 0:
            QMessageBox.information(self, "information", "请输入旧密码！")
        else:
            results = sql.do("select password from admin where ano=%s" % user.current_admin)
            now_password = str(results[0][0])
            if now_password == old_password:
                if len(new_password) != 0:
                    if new_password_1 != new_password:
                        QMessageBox.information(self, "information", "两次密码不同，请确认！")
                    else:
                        sql.do("update admin set password='%s' where ano=%s" % (new_password, user.current_admin))
                        QMessageBox.information(self, "information", "修改成功！")
                else:
                    QMessageBox.information(self, "information", "新密码不能为空，请输入！")
            else:
                QMessageBox.information(self, "information", "旧密码错误，请重新输入！")

        # print("change password")
        # pass

    def search_food(self):
        fname = self.tableWidget.item(1, 0).text()
        wno = self.tableWidget.item(1, 1).text()
        price = self.tableWidget.item(1, 2).text()
        wname = self.tableWidget.item(1, 3).text()
        state = self.tableWidget.item(1, 4).text()

        # 动态生成sql查询语句
        search_sql = "select * from menu where " \
                     "(fname like '%{0}%' or '{0}'='') " \
                     "and (wno='{1}' or '{1}'='') " \
                     "and (price='{2}' or '{2}'='') " \
                     "and (wname='{3}' or '{3}'='') " \
                     "and (state='{4}' or '{4}'='')".format(fname, wno, price, wname, state)

        results = sql.do(search_sql)
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(len(results) + 1)

        for i in range(len(results)):
            self.tableWidget_2.setVerticalHeaderItem(i + 1, QTableWidgetItem(str(i + 1)))
        for i in range(len(results)):
            for j in range(len(results[i])):
                self.tableWidget_2.setItem(i + 1, j, QTableWidgetItem(str(results[i][j])))
        # print("search")
        # pass

    def add_food(self):
        try:
            fname = self.tableWidget.item(1, 0).text()
            wno = self.tableWidget.item(1, 1).text()
            price = self.tableWidget.item(1, 2).text()

            add_sql = "insert into food values('%s',%s,%s,'在售')" % (fname,wno,price)
            sql.do(add_sql)
            QMessageBox.information(self,"informaiton","添加成功！")
            self.show_menu()
        except:
            pass

    def change_food(self):
        try:
            fname = self.tableWidget.item(1, 0).text()
            wno = self.tableWidget.item(1, 1).text()
            price = self.tableWidget.item(1, 2).text()

            if len(fname)==0:
                QMessageBox.information(self,"information","请输入想要修改属性的饭菜名！")
            else:
                if len(wno)!=0:
                    sql.do("update food set wno=%s where fname='%s'" % (wno,fname))
                    QMessageBox.information(self, "information", "窗口修改成功！")
                if len(price)!=0:
                    sql.do("update food set price=%s where fname='%s'" % (price, fname))
                    QMessageBox.information(self, "information", "价格修改成功！")

                self.show_menu()
        except:
            pass

    def change_state(self):
        try:
            current_food_fname=self.tableWidget_2.item(self.tableWidget_2.currentRow(),0).text()
            results=sql.do("select state from food where fname='%s'" % (current_food_fname))
            current_food_state=str(results[0][0])
            if current_food_state!="在售":
                sql.do("update food set state='%s' where fname='%s'" % ("在售",current_food_fname))
                QMessageBox.information(self,"information","上架成功！")
            else:
                sql.do("update food set state='%s' where fname='%s'" % ("下架", current_food_fname))
                QMessageBox.information(self, "information", "下架成功！")

            self.show_menu()
            # print(current_food_state)
        except:
            pass

    def delete_food(self):
        try:
            current_food_fname=self.tableWidget_2.item(self.tableWidget_2.currentRow(),0).text()
            sql.do("delete from food where fname='%s'" % (current_food_fname))
            QMessageBox.information(self,"information","删除成功！")
            self.show_menu()
        except:
            pass

    def change_wname(self):
        try:
            current_wno = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
            current_wname=self.tableWidget.item(self.tableWidget.currentRow(), 3).text()
            print(current_wno,current_wname)
            if len(current_wname)==0:
                QMessageBox.information(self,"information","请输入窗口号！")
            else:
                sql.do("update windows set wname='%s' where wno=%s" % (current_wname,current_wno))
                QMessageBox.information(self, "information", "修改窗口名成功！")
                self.show_menu()
        except:
            pass

def main():
    app=QApplication(sys.argv)
    window=Login()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
