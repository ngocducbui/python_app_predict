from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QStyledItemDelegate, QAction, QLineEdit
import sys
from database import connect_database
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from openpyxl import Workbook, load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from source import register
from source import reset_password
from source import admin
from source import import_screen
from source import predict
import common as cm


class UI_login_3(QMainWindow):
    def __init__(self, parent=None):
        self.image_link = ''

        super(UI_login_3, self).__init__(parent)
        # self.database_config_obj = None

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1155, 916)
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 50, 901, 761))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 461, 761))
        self.label.setStyleSheet("background-colora:rgb(0, 0, 0, 80);\n"
                                 "border-image: url(..//images/2.jpg);\n"
                                 "border-top-left-radius: 50px;\n"
                                 "\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(460, 0, 441, 761))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
                                   "border-bottom-right-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_4.setGeometry(QtCore.QRect(840, 0, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-top-left-radius:5px;border-bottom-left-radius:5px\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_4:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_4:pressed{\n"
            "    padding-left:10px;\n"
            "    padding-top:10px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "\n"
            "")

        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.clicked.connect(self.change)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 0, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "        border-top-right-radius:5px;border-bottom-right-radius:5px\n"
            "\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_6:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_6:pressed{\n"
            "    padding-left:10px;\n"
            "    padding-top:10px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "\n"
            "")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(460, 70, 531, 641))
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(150, 80, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(11, 34, 57);")
        self.label_3.setObjectName("label_3")
        self.register_2 = QtWidgets.QLabel(self.widget_2)
        self.register_2.hide()
        self.register_2.setGeometry(QtCore.QRect(150, 600, 161, 16))
        self.register_2.setStyleSheet("text-decoration:underline;\n"
                                      "color: blue")
        self.register_2.setObjectName("register_2")
        self.txt_username = QtWidgets.QLineEdit(self.widget_2)
        self.txt_username.setGeometry(QtCore.QRect(40, 210, 361, 41))
        self.txt_username.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:none;\n"
                                        "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                        "color:rgba(0, 0, 0, 240);\n"
                                        "padding-bottom:7px")
        self.txt_username.setObjectName("txt_username")
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setGeometry(QtCore.QRect(40, 370, 131, 20))
        self.checkBox.setObjectName("checkBox")
        self.forget_password = QtWidgets.QLabel(self.widget_2)
        self.forget_password.mousePressEvent = self.reset_pass
        self.forget_password.setStyleSheet("text-decoration:underline;\n"
                                           "color: blue")
        self.forget_password.setGeometry(QtCore.QRect(300, 410, 201, 20))
        self.forget_password.setObjectName("forget_password")
        self.txt_passwprd = QtWidgets.QLineEdit(self.widget_2)
        self.txt_passwprd.setEchoMode(QLineEdit.Password)
        self.txt_passwprd.setGeometry(QtCore.QRect(40, 310, 361, 41))
        self.txt_passwprd.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:none;\n"
                                        "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                        "color:rgba(0, 0, 0, 240);\n"
                                        "padding-bottom:7px")
        self.txt_passwprd.setObjectName("txt_passwprd")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.clicked.connect(self.login)
        self.pushButton.setGeometry(QtCore.QRect(90, 500, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:5px;\n"
            "}\n"
            "\n"
            "QPushButton#pushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "QPushButton#pushButton:pressed{\n"
            "    padding-left:10px;\n"
            "    padding-top:10px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "    color:rgba(85, 98, 112, 255);\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
            "    color: rgba(131, 96, 53, 255);\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    color:rgba(91, 88, 53, 255);\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
            "    background-color: rgba(0, 0, 0, 0);\n"
            "    color:rgba(85, 98, 112, 255);\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
            "    color: rgba(131, 96, 53, 255);\n"
            "")
        self.pushButton.setObjectName("pushButton")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(460, 40, 421, 711))
        self.widget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_3.setObjectName("widget_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(140, 0, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(11, 34, 57);")
        self.label_4.setObjectName("label_4")
        self.txt_fullname = QtWidgets.QLineEdit(self.widget_3)
        self.txt_fullname.setGeometry(QtCore.QRect(30, 50, 371, 41))
        self.txt_fullname.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:none;\n"
                                        "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                        "color:rgba(0, 0, 0, 240);\n"
                                        "padding-bottom:7px")
        self.txt_fullname.setText("")
        self.txt_fullname.setObjectName("txt_fullname")
        self.txt_username_2 = QtWidgets.QLineEdit(self.widget_3)
        self.txt_username_2.setGeometry(QtCore.QRect(30, 360, 371, 41))
        self.txt_username_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                          "border:none;\n"
                                          "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                          "color:rgba(0, 0, 0, 240);\n"
                                          "padding-bottom:7px")
        self.txt_username_2.setText("")
        self.txt_username_2.setObjectName("txt_username_2")
        self.txt_passwprd_2 = QtWidgets.QLineEdit(self.widget_3)
        self.txt_passwprd_2.setEchoMode(QLineEdit.Password)

        self.txt_passwprd_2.setGeometry(QtCore.QRect(30, 420, 371, 41))
        self.txt_passwprd_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                          "border:none;\n"
                                          "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                          "color:rgba(0, 0, 0, 240);\n"
                                          "padding-bottom:7px")
        self.txt_passwprd_2.setText("")
        self.txt_passwprd_2.setObjectName("txt_passwprd_2")
        self.txt_email = QtWidgets.QLineEdit(self.widget_3)
        self.txt_email.setGeometry(QtCore.QRect(30, 230, 371, 41))
        self.txt_email.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                     "border:none;\n"
                                     "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                     "color:rgba(0, 0, 0, 240);\n"
                                     "padding-bottom:7px")
        self.txt_email.setText("")
        self.txt_email.setObjectName("txt_email")
        self.txt_phone = QtWidgets.QLineEdit(self.widget_3)
        self.txt_phone.setGeometry(QtCore.QRect(30, 170, 371, 41))
        self.txt_phone.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                     "border:none;\n"
                                     "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                     "color:rgba(0, 0, 0, 240);\n"
                                     "padding-bottom:7px")
        self.txt_phone.setText("")
        self.txt_phone.setObjectName("txt_phone")
        self.date = QtWidgets.QDateEdit(self.widget_3)
        self.date.setGeometry(QtCore.QRect(30, 120, 371, 31))
        self.date.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                "border:none;\n"
                                "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                "color:rgba(0, 0, 0, 240);\n"
                                "padding-bottom:7px")
        self.date.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.date.setProperty("showGroupSeparator", False)
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.txt_adress = QtWidgets.QLineEdit(self.widget_3)
        self.txt_adress.setGeometry(QtCore.QRect(30, 290, 371, 41))
        self.txt_adress.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px")
        self.txt_adress.setText("")
        self.txt_adress.setObjectName("txt_adress")
        self.txt_con_pass = QtWidgets.QLineEdit(self.widget_3)
        self.txt_con_pass.setEchoMode(QLineEdit.Password)
        self.txt_con_pass.setGeometry(QtCore.QRect(30, 480, 371, 41))
        self.txt_con_pass.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:none;\n"
                                        "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                        "color:rgba(0, 0, 0, 240);\n"
                                        "padding-bottom:7px")
        self.txt_con_pass.setText("")
        self.txt_con_pass.setObjectName("txt_con_pass")
        self.check_box_agree = QtWidgets.QCheckBox(self.widget_3)
        self.check_box_agree.setGeometry(QtCore.QRect(130, 590, 251, 20))
        self.check_box_agree.setObjectName("check_box_agree")
        self.txt_avatar = QtWidgets.QLineEdit(self.widget_3)
        self.txt_avatar.setEnabled(False)
        self.txt_avatar.setGeometry(QtCore.QRect(30, 540, 261, 41))
        self.txt_avatar.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px")
        self.txt_avatar.setText("")
        self.txt_avatar.setObjectName("txt_avatar")
        self.btn_avatar = QtWidgets.QPushButton(self.widget_3)
        self.btn_avatar.clicked.connect(self.upload_image)
        self.btn_avatar.setGeometry(QtCore.QRect(310, 540, 89, 31))
        self.btn_avatar.setObjectName("btn_avatar")
        self.label_error = QtWidgets.QLabel(self.widget_3)
        self.label_error.setStyleSheet("text-decoration:underline;\n"
                                       "color: red")
        self.label_error.setGeometry(QtCore.QRect(20, 620, 401, 20))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_error.setFont(font)
        self.label_error.setObjectName("label_error")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.clicked.connect(self.register)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 650, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:5px;\n"
            "}\n"
            "\n"
            "QPushButton#pushButton_2:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "QPushButton#pushButton-2:pressed{\n"
            "    padding-left:10px;\n"
            "    padding-top:10px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "\n"
            "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1155, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.widget_3.hide()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Login System"))
        self.pushButton_4.setText(_translate("MainWindow", "X"))
        self.pushButton_6.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "SIGN IN"))
        self.register_2.setText(_translate("MainWindow", "You don\'t have an account?"))
        self.txt_username.setPlaceholderText(_translate("MainWindow", "User name"))
        self.checkBox.setText(_translate("MainWindow", "Remember me?"))
        self.forget_password.setText(_translate("MainWindow", "Forget Password"))
        self.txt_passwprd.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Sign In"))
        self.label_4.setText(_translate("MainWindow", "REGISTER "))
        self.txt_fullname.setPlaceholderText(_translate("MainWindow", "Full Name"))
        self.txt_username_2.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.txt_passwprd_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.txt_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.txt_phone.setPlaceholderText(_translate("MainWindow", "Phone Number"))
        self.date.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.txt_adress.setPlaceholderText(_translate("MainWindow", "Address"))
        self.txt_con_pass.setPlaceholderText(_translate("MainWindow", "Confirm password"))
        self.check_box_agree.setText(_translate("MainWindow", "I agree to the Terms and Conditions"))
        self.txt_avatar.setPlaceholderText(_translate("MainWindow", "Avatar"))
        self.btn_avatar.setText(_translate("MainWindow", "Choose File"))
        self.label_error.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "Sign In"))

    def change(self):
        if self.pushButton_6.isChecked():
            self.widget_2.hide()
            self.widget_3.show()
            self.pushButton_6.setText('<')
        else:
            self.widget_3.hide()
            self.widget_2.show()
            self.pushButton_6.setText('>')


    def login(self):
        try:
            username = self.txt_username.text()
            password = self.txt_passwprd.text()
            if len(username) == 0 or len(password) == 0 or (len(username) and len(password) == 0):
                QMessageBox.information(self, 'Login', 'Please enter all data fields!', QMessageBox.Close)
            else:
                data = connect_database.login_3(username, password)
                if len(data) == 0:
                    QMessageBox.information(self, 'Login', 'Wrong username or password!', QMessageBox.Close)
                else:
                    if data[0][0] == '1':
                        self.ui = QMainWindow()
                        self.ui = admin.UI_admin()
                        self.ui.setupUi()
                        self.ui.show()
                        self.ui.label_2.setText(data[0][1])
                        self.hide()
                    else:
                        self.ui = QMainWindow()
                        self.ui = import_screen.Ui_import_window()
                        self.ui.setupUi()
                        self.ui.show()
                        self.ui.label_3.setText(data[0][1])
                        self.ui.label_id.setText(data[0][2])
                        self.hide()
                        # self.ui.add_new_btn.clicked.connect(self.open_predict)
        except Exception as err:
            QMessageBox.information(self, 'System',
                                    'An error occurred while logging in system. Please try again!',
                                    QMessageBox.Close)

    def register(self):
        try:
            fullname = self.txt_fullname.text()
            dob = self.date.dateTime().toPyDateTime().date()
            phone = self.txt_phone.text()
            email = self.txt_email.text()
            address = self.txt_adress.text()
            username = self.txt_username_2.text()
            password = self.txt_passwprd_2.text()
            con_pass = self.txt_con_pass.text()
            date_now = datetime.now().date()
            image_link = self.image_link
            if image_link != '':
                with open(image_link, 'rb') as File:
                    BinaryData = File.read()
            else:
                BinaryData = None
            role = str(0)
            if all(v != '' for v in [fullname, dob, phone, email, address, username, password]):
                if con_pass == password:
                    if dob < date_now:
                        if cm.check_phone(phone):
                            if cm.check_email(email):
                                try:
                                    if self.check_box_agree.isChecked():
                                        if connect_database.register(fullname, dob, phone, email, address, username,
                                                                     password, role, BinaryData):
                                            QMessageBox.information(self, 'Register',
                                                                    f'Successful registration. Welcome {fullname}',
                                                                    QMessageBox.Close)
                                            # self.widget_3.hide()
                                            # self.widget_2.show()
                                            # self.date.setDate()
                                            self.txt_fullname.setText('')
                                            self.txt_phone.setText('')
                                            self.txt_email.setText('')
                                            self.txt_adress.setText('')
                                            self.txt_username_2.setText('')
                                            self.txt_passwprd_2.setText('')
                                            self.txt_con_pass.setText('')
                                            self.txt_avatar.setText('')
                                            self.change()
                                            # self.pushButton_6.isChecked()


                                        else:
                                            # QMessageBox.information(self, 'Register', 'Username already exists',
                                            #                         QMessageBox.Close)
                                            self.label_error.setText(' ')
                                            self.label_error.setText('Username already exists')

                                    else:
                                        self.label_error.setText(' ')
                                        self.label_error.setText('Please click the agree button')

                                        # QMessageBox.information(self, 'Register', 'Please click the agree button',
                                        #                         QMessageBox.Close)
                                except Exception as err:
                                    QMessageBox.information(self, 'Register', 'Register failed!\n'
                                                                              f'{str(err)}',
                                                            QMessageBox.Close)
                            else:
                                self.label_error.setText(' ')
                                self.label_error.setText('Wrong email address format!')
                                # QMessageBox.information(self, 'Register', 'Wrong email address format!',
                                # QMessageBox.Close)
                        else:
                            self.label_error.setText(' ')
                            self.label_error.setText('Wrong phone number format!')
                            # QMessageBox.information(self, 'Register', 'Wrong phone number format!', QMessageBox.Close)
                    else:
                        self.label_error.setText(' ')
                        self.label_error.setText('Date of birth cannot be greater than current date!')
                        # QMessageBox.information(self, 'Register', 'Date of birth cannot be greater than current date!',
                        # QMessageBox.Close)
                else:
                    self.label_error.setText(' ')
                    self.label_error.setText('Passwords do not match!')
                    # QMessageBox.information(self, 'Register', 'Passwords do not match!', QMessageBox.Close)
            else:
                self.label_error.setText(' ')
                self.label_error.setText('Please fill in all fields!')
                # QMessageBox.information(self, 'Register', 'Please fill in all fields!', QMessageBox.Close)
        except Exception as err:
            QMessageBox.information(self, 'Register', 'Please fill in all fields!\n'
                                                      f'{str(err)}', QMessageBox.Close)

    def upload_image(self):
        root = tk.Tk()
        root.withdraw()
        f_types = [("Image File", '.jpg .png .jpeg .webp')]
        file_path = filedialog.askopenfilename(filetypes=f_types)
        self.image_link = file_path
        if file_path != '':
            self.txt_avatar.setText(file_path)
        else:
            self.txt_avatar.setText('')

    def reset_pass(self, event):
        try:
            self.ui = QMainWindow()
            self.ui = reset_password.UI_reset_password()
            self.ui.setupUi()
            self.ui.show()

        except Exception as err:
            QMessageBox.information(self, 'System',
                                    'An error occurred while opening reset password. Please try again!\n'
                                    f'{str(err)}',
                                    QMessageBox.Close)

    def close(self):
        try:
            ques = QMessageBox.question(self, 'System', f'Are you sure you want to exit the program?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ques == QMessageBox.Yes:
                app = QtWidgets.QApplication(sys.argv)
                app.instance().quit()
            else:
                pass
        except Exception as err:
            QMessageBox.information(self, 'System', 'An error occurred while logging out. Please try again later!\n'
                                                    f'{str(err)}',
                                    QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_login_3()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
