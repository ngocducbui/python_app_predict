import sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from source import predict
from source import login_3
from source import profile_user
from source import percentage
from source import logistic_regression
from source import random_forest
from source import linear_regression
from source import knn
from source import decision_tree
from database import connect_database
import machine_learning
import pathlib
import gdown

class Ui_import_window(QMainWindow):

    def __init__(self, parent=None):
        super(Ui_import_window, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("main_window")
        self.resize(1051, 765)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowIcon(QtGui.QIcon("../icon/logo.png"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 30, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.import_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_btn.setGeometry(QtCore.QRect(912, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.import_btn.setFont(font)
        self.import_btn.setObjectName("import_btn")
        self.import_btn.clicked.connect(self.import_data)
        self.import_btn.setIcon(QtGui.QIcon('../icon/import.png'))
        self.import_btn.setStyleSheet("background-color:rgb(94, 186, 125)")

        self.add_new_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_btn.setStyleSheet("background-color:rgb(218, 91, 11)")
        self.add_new_btn.setGeometry(QtCore.QRect(690, 160, 93, 41))
        self.add_new_btn.hide()
        self.add_new_btn.clicked.connect(self.predict)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_new_btn.setFont(font)
        self.add_new_btn.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.add_new_btn.setObjectName("add_new_btn")
        self.data_table = QtWidgets.QTableWidget(self.centralwidget)
        self.data_table.setGeometry(QtCore.QRect(20, 90, 1011, 391))
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(35)
        self.data_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.data_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(34, item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 0, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(970, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        # self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(720, 0, 81, 21))
        self.label_id.hide()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.shape = QtWidgets.QLabel(self.centralwidget)
        self.shape.setGeometry(QtCore.QRect(150, 70, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.shape.setFont(font)
        self.shape.setText("")
        self.shape.setObjectName("shape")
        self.tab_ml = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_ml.setGeometry(QtCore.QRect(20, 490, 1011, 231))
        self.tab_ml.setObjectName("tab_ml")
        self.data = QtWidgets.QWidget()
        self.data.setObjectName("data")
        self.cbo_data = QtWidgets.QComboBox(self.data)
        self.cbo_data.setEnabled(False)
        self.cbo_data.setGeometry(QtCore.QRect(20, 130, 321, 31))
        self.cbo_data.setObjectName("cbo_data")
        self.cbo_data.addItem("")
        self.cbo_data.addItem("")
        self.cbo_data.addItem("")
        self.cbo_data.addItem("")
        self.cbo_data.addItem("")
        self.cbo_data.addItem("")
        self.cbo_data.addItem("")
        self.cbo_data.addItem("")
        self.cbo_data.addItem("")

        self.btn_view = QtWidgets.QPushButton(self.data)
        self.btn_view.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.btn_view.setEnabled(False)
        self.btn_view.clicked.connect(self.view)
        self.btn_view.setIcon(QtGui.QIcon('../icon/view.png'))
        self.btn_view.setGeometry(QtCore.QRect(380, 130, 89, 31))
        self.btn_view.setObjectName("btn_view")
        self.label_5 = QtWidgets.QLabel(self.data)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_7 = QtWidgets.QLabel(self.data)
        self.label_7.setGeometry(QtCore.QRect(510, 40, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.data)
        self.line.setGeometry(QtCore.QRect(490, 0, 16, 201))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox_2 = QtWidgets.QComboBox(self.data)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.activated.connect(self.corr)

        self.comboBox_2.setGeometry(QtCore.QRect(540, 130, 321, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.data)
        self.pushButton.setStyleSheet("background-color:rgb(94, 186, 125)")

        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.view_corr)
        self.pushButton.setIcon(QtGui.QIcon('../icon/view.png'))
        self.pushButton.setGeometry(QtCore.QRect(900, 130, 89, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.data)
        # self.label_8.hide()
        self.label_8.setGeometry(QtCore.QRect(520, 70, 471, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.data)
        self.label_9.setStyleSheet("text-decoration:underline;\n"
                                   "color: blue")
        self.label_9.mousePressEvent = self.clear
        self.label_9.setGeometry(QtCore.QRect(970, 0, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.data)
        self.label_10.setStyleSheet("color: red")
        self.label_10.setGeometry(QtCore.QRect(520, 110, 471, 20))
        self.label_10.setObjectName("label_10")
        self.tab_ml.addTab(self.data, "")
        self.Training = QtWidgets.QWidget()
        self.Training.setObjectName("Training")
        self.progressBar = QtWidgets.QProgressBar(self.Training)
        self.progressBar.hide()
        self.progressBar.setGeometry(QtCore.QRect(220, 160, 630, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(self.Training)
        self.label_6.setGeometry(QtCore.QRect(140, 60, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_storage_link = QtWidgets.QLabel(self.Training)
        self.label_storage_link.hide()
        self.label_6.setGeometry(QtCore.QRect(140, 60, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_storage_link.setFont(font)
        self.label_storage_link.setObjectName("label_6")
        self.btn_train = QtWidgets.QPushButton(self.Training)
        self.btn_train.setIcon(QtGui.QIcon('../icon/start.png'))
        self.btn_train.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.btn_train.clicked.connect(self.train)
        self.btn_train.setEnabled(False)
        self.btn_train.setGeometry(QtCore.QRect(450, 110, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_train.setFont(font)
        self.btn_train.setObjectName("btn_train")
        self.btn_pridict = QtWidgets.QPushButton(self.Training)
        self.btn_pridict.hide()
        self.btn_pridict.clicked.connect(self.pridict)
        self.btn_pridict.setEnabled(False)
        self.btn_pridict.setGeometry(QtCore.QRect(760, 50, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_pridict.setFont(font)
        self.btn_pridict.setObjectName("btn_pridict")
        self.comboBox = QtWidgets.QComboBox(self.Training)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(330, 50, 371, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.Training)
        self.label_11.setEnabled(False)
        self.label_11.setStyleSheet("text-decoration:underline;\n"
                                    "color: blue")
        self.label_11.mousePressEvent = self.percentage
        self.label_11.setGeometry(QtCore.QRect(610, 90, 251, 16))
        self.label_11.setObjectName("label_11")
        self.tab_ml.addTab(self.Training, "")
        self.import_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.import_btn_2.setGeometry(QtCore.QRect(750, 50, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.import_btn_2.setFont(font)
        self.import_btn_2.setObjectName("import_btn_2")
        self.import_btn_2.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.import_btn_2.clicked.connect(self.download)
        self.import_btn_2.setIcon(QtGui.QIcon('../icon/download.png'))
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 25))
        self.menubar.setObjectName("menubar")
        self.menuProfile = QtWidgets.QMenu(self.menubar)
        self.menuProfile.setObjectName("menuProfile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionUpdate_profile = QtWidgets.QAction(self)
        self.actionUpdate_profile.triggered.connect(self.update_profile)
        self.actionUpdate_profile.setIcon(QtGui.QIcon('../icon/profile.png'))
        self.actionUpdate_profile.setObjectName("actionUpdate_profile")
        self.actionSign_out = QtWidgets.QAction(self)
        self.actionSign_out.setIcon(QtGui.QIcon('../icon/sign-out.png'))
        self.actionSign_out.triggered.connect(self.sign_out)
        self.actionSign_out.setObjectName("actionSign_out")
        self.actionAbout_us = QtWidgets.QAction(self)
        self.actionAbout_us.setIcon(QtGui.QIcon('../icon/contact.png'))
        self.actionAbout_us.triggered.connect(self.about_us)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.menuProfile.addAction(self.actionUpdate_profile)
        self.menuProfile.addAction(self.actionSign_out)
        self.menuAbout.addAction(self.actionAbout_us)
        self.menubar.addAction(self.menuProfile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.retranslateUi()
        self.tab_ml.setCurrentIndex(0)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("main_window", "Machine Learning"))
        self.label.setText(_translate("main_window", "MACHINE LEARNING"))
        self.import_btn.setText(_translate("main_window", "Import"))
        self.add_new_btn.setText(_translate("main_window", "Predict"))
        item = self.data_table.horizontalHeaderItem(0)
        item.setText(_translate("main_window", "Marital status"))
        item = self.data_table.horizontalHeaderItem(1)
        item.setText(_translate("main_window", "Application mode"))
        item = self.data_table.horizontalHeaderItem(2)
        item.setText(_translate("main_window", "Application order"))
        item = self.data_table.horizontalHeaderItem(3)
        item.setText(_translate("main_window", "Course"))
        item = self.data_table.horizontalHeaderItem(4)
        item.setText(_translate("main_window", "Daytime/evening attendance"))
        item = self.data_table.horizontalHeaderItem(5)
        item.setText(_translate("main_window", "Previous qualification"))
        item = self.data_table.horizontalHeaderItem(6)
        item.setText(_translate("main_window", "Nacionality"))
        item = self.data_table.horizontalHeaderItem(7)
        item.setText(_translate("main_window", "Mother\'s qualification"))
        item = self.data_table.horizontalHeaderItem(8)
        item.setText(_translate("main_window", "Father\'s qualification"))
        item = self.data_table.horizontalHeaderItem(9)
        item.setText(_translate("main_window", "Mother\'s occupation"))
        item = self.data_table.horizontalHeaderItem(10)
        item.setText(_translate("main_window", "Father\'s occupation"))
        item = self.data_table.horizontalHeaderItem(11)
        item.setText(_translate("main_window", "Displaced"))
        item = self.data_table.horizontalHeaderItem(12)
        item.setText(_translate("main_window", "Educational special needs"))
        item = self.data_table.horizontalHeaderItem(13)
        item.setText(_translate("main_window", "Debtor"))
        item = self.data_table.horizontalHeaderItem(14)
        item.setText(_translate("main_window", "Tuition fees up to date"))
        item = self.data_table.horizontalHeaderItem(15)
        item.setText(_translate("main_window", "Gender"))
        item = self.data_table.horizontalHeaderItem(16)
        item.setText(_translate("main_window", "Scholarship holder"))
        item = self.data_table.horizontalHeaderItem(17)
        item.setText(_translate("main_window", "Age at enrollment"))
        item = self.data_table.horizontalHeaderItem(18)
        item.setText(_translate("main_window", "International"))
        item = self.data_table.horizontalHeaderItem(19)
        item.setText(_translate("main_window", "Curricular units 1st sem (credited)"))
        item = self.data_table.horizontalHeaderItem(20)
        item.setText(_translate("main_window", "Curricular units 1st sem (enrolled)"))
        item = self.data_table.horizontalHeaderItem(21)
        item.setText(_translate("main_window", "Curricular units 1st sem (evaluations)"))
        item = self.data_table.horizontalHeaderItem(22)
        item.setText(_translate("main_window", "Curricular units 1st sem (approved)"))
        item = self.data_table.horizontalHeaderItem(23)
        item.setText(_translate("main_window", "Curricular units 1st sem (grade)"))
        item = self.data_table.horizontalHeaderItem(24)
        item.setText(_translate("main_window", "Curricular Units 1st Sem (without Evaluations)"))
        item = self.data_table.horizontalHeaderItem(25)
        item.setText(_translate("main_window", "Curricular Units 2nd Sem (credited)"))
        item = self.data_table.horizontalHeaderItem(26)
        item.setText(_translate("main_window", "Curricular Units 2nd Sem (enrolled)"))
        item = self.data_table.horizontalHeaderItem(27)
        item.setText(_translate("main_window", "Curricular Units 2nd Sem (evaluations)"))
        item = self.data_table.horizontalHeaderItem(28)
        item.setText(_translate("main_window", "Curricular Units 2nd Sem (approved)"))
        item = self.data_table.horizontalHeaderItem(29)
        item.setText(_translate("main_window", "Curricular Units 2nd Sem (grade)"))
        item = self.data_table.horizontalHeaderItem(30)
        item.setText(_translate("main_window", "Curricular Units 2nd Sem (without Evaluations)"))
        item = self.data_table.horizontalHeaderItem(31)
        item.setText(_translate("main_window", "Unemployment Rate"))
        item = self.data_table.horizontalHeaderItem(32)
        item.setText(_translate("main_window", "Inflation Rate"))
        item = self.data_table.horizontalHeaderItem(33)
        item.setText(_translate("main_window", "Inflation Rate"))
        item = self.data_table.horizontalHeaderItem(34)
        item.setText(_translate("main_window", "Target"))
        self.label_2.setText(_translate("main_window", "Welcome: "))
        self.label_3.setText(_translate("main_window", "User name"))
        self.label_id.setText(_translate("main_window", "ID"))
        self.label_4.setText(_translate("main_window", "Shape of dataset: "))
        self.cbo_data.setItemText(0, _translate("main_window", "Percentage of Student Target"))
        self.cbo_data.setItemText(1, _translate("main_window", "Number of student target by Genders"))
        self.cbo_data.setItemText(2, _translate("main_window", "Number of student target by Marital Status"))
        self.cbo_data.setItemText(3, _translate("main_window", "Number of student enrolled by Ages"))
        self.cbo_data.setItemText(4, _translate("main_window", "Dropout percentage by Ages"))
        self.cbo_data.setItemText(5, _translate("main_window", "Number of student with Educational Special Needs"))
        self.cbo_data.setItemText(6, _translate("main_window",
                                                "Statistics/comparison in Number of student Target by Debt"))
        self.cbo_data.setItemText(7, _translate("main_window", "Rate of Unemployment student"))
        self.cbo_data.setItemText(8, _translate("main_window", "Correlation heatmap between variables"))
        #self.cbo_data.setItemText(9, _translate("main_window",
                                                #"Assess the accuracy of the model through the confusion matrix scale"))
        self.btn_view.setText(_translate("main_window", "View"))
        self.label_5.setText(_translate("main_window", "Analyst the data from the import file:"))

        self.label_7.setText(_translate("main_window", "Correlation chart of columns:"))
        self.comboBox_2.setItemText(0, _translate("main_window", "Marital status"))
        self.comboBox_2.setItemText(1, _translate("main_window", "Application mode"))
        self.comboBox_2.setItemText(2, _translate("main_window", "Application order"))
        self.comboBox_2.setItemText(3, _translate("main_window", "Course"))
        self.comboBox_2.setItemText(4, _translate("main_window", "Daytime/evening attendance"))
        self.comboBox_2.setItemText(5, _translate("main_window", "Previous qualification"))
        self.comboBox_2.setItemText(6, _translate("main_window", "Mother\'s qualification"))
        self.comboBox_2.setItemText(7, _translate("main_window", "Father\'s qualification"))
        self.comboBox_2.setItemText(8, _translate("main_window", "Mother\'s occupation"))
        self.comboBox_2.setItemText(9, _translate("main_window", "Father\'s occupation"))
        self.comboBox_2.setItemText(10, _translate("main_window", "Displaced"))
        self.comboBox_2.setItemText(11, _translate("main_window", "Educational special needs"))
        self.comboBox_2.setItemText(12, _translate("main_window", "Debtor"))
        self.comboBox_2.setItemText(13, _translate("main_window", "Tuition fees up to date"))
        self.comboBox_2.setItemText(14, _translate("main_window", "Gender"))
        self.comboBox_2.setItemText(15, _translate("main_window", "Scholarship holder"))
        self.comboBox_2.setItemText(16, _translate("main_window", "Age at enrollment"))
        self.comboBox_2.setItemText(17, _translate("main_window", "Curricular units 1st sem (credited)"))
        self.comboBox_2.setItemText(18, _translate("main_window", "Curricular units 1st sem (enrolled)"))
        self.comboBox_2.setItemText(19, _translate("main_window", "Curricular units 1st sem (evaluations)"))
        self.comboBox_2.setItemText(20, _translate("main_window", "Curricular units 1st sem (approved)"))
        self.comboBox_2.setItemText(21, _translate("main_window", "Curricular units 1st sem (grade)"))
        self.comboBox_2.setItemText(22, _translate("main_window", "Curricular units 1st sem (without evaluations)"))
        self.comboBox_2.setItemText(23, _translate("main_window", "Curricular units 2nd sem (credited)"))
        self.comboBox_2.setItemText(24, _translate("main_window", "Curricular units 2nd sem (enrolled)"))
        self.comboBox_2.setItemText(25, _translate("main_window", "Curricular units 2nd sem (evaluations)"))
        self.comboBox_2.setItemText(26, _translate("main_window", "Curricular units 2nd sem (approved)"))
        self.comboBox_2.setItemText(27, _translate("main_window", "Curricular units 2nd sem (grade)"))
        self.comboBox_2.setItemText(28, _translate("main_window", "Curricular units 2nd sem (without evaluations)"))
        self.comboBox_2.setItemText(29, _translate("main_window", "Unemployment rate"))
        self.comboBox_2.setItemText(30, _translate("main_window", "Inflation rate"))
        self.comboBox_2.setItemText(31, _translate("main_window", "GDP"))
        self.pushButton.setText(_translate("main_window", "View"))
        self.label_8.setText(_translate("main_window", ""))
        self.label_9.setText(_translate("main_window", "Clear"))
        self.label_10.setText(_translate("main_window", ""))
        self.tab_ml.setTabText(self.tab_ml.indexOf(self.data), _translate("main_window", "Data Analyst"))
        self.label_6.setText(_translate("main_window", "Traning:"))
        self.label_6.setText(_translate("main_window", "Algorithm selection:"))
        self.btn_train.setText(_translate("main_window", "Start"))
        self.btn_pridict.setText(_translate("main_window", "Predict"))
        self.comboBox.setItemText(0, _translate("main_window", "Random Forest Classifier"))
        self.comboBox.setItemText(1, _translate("main_window", "Logistic Regression"))
        self.comboBox.setItemText(2, _translate("main_window", "Decision Tree Classifier"))
        self.comboBox.setItemText(3, _translate("main_window", "K-Nearest Neighbors Classifier"))
        self.label_storage_link.setText(_translate("main_window", "save link import"))
        self.btn_train.setText(_translate("main_window", "Start "))
        self.btn_pridict.setText(_translate("main_window", "Pridict"))
        self.tab_ml.setTabText(self.tab_ml.indexOf(self.Training), _translate("main_window", "Traning Model"))
        self.menuProfile.setTitle(_translate("main_window", "Profile"))
        self.menuAbout.setTitle(_translate("main_window", "About"))
        self.actionUpdate_profile.setText(_translate("main_window", "Update profile"))
        self.actionSign_out.setText(_translate("main_window", "Sign out"))
        self.actionAbout_us.setText(_translate("main_window", "About us"))
        self.label_11.setText(_translate("main_window", "Don\'t know which algorithm to choose?"))
        self.import_btn_2.setText(_translate("main_window", "Download Data"))
    def import_data(self):
        try:
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
            self.label_storage_link.setText(file_path)
            if file_path == '':
                pass
            else:
                extension = pathlib.Path(file_path).suffix
                if extension == '.csv' or extension == '.xlsx':
                    if file_path is not None:
                        if extension == '.csv':
                            self.data = pd.read_csv(file_path)
                        else:
                            self.data = pd.read_excel(file_path)
                        self.data_table.setRowCount(len(self.data))
                        for i in range(len(self.data)):
                            for j in range(35):
                                self.data_table.setItem(
                                    i, j, QtWidgets.QTableWidgetItem(str(self.data.iloc[i, j])))
                        self.cbo_data.setEnabled(True)
                        self.btn_view.setEnabled(True)
                        self.btn_train.setEnabled(True)
                        self.comboBox_2.setEnabled(True)
                        self.pushButton.setEnabled(True)
                        self.comboBox.setEnabled(True)
                        self.label_11.setEnabled(True)
                        self.shape.setText(machine_learning.shape(file_path, extension))
                else:
                    QMessageBox.information(self, 'System', 'Please import into excel file!', QMessageBox.Close)
        except:
            QMessageBox.information(self, 'System', 'Error import. Please try again!', QMessageBox.Close)

    def predict(self):
        try:
            self.ui = QMainWindow()
            self.ui = predict.Ui_predict_window()
            self.ui.setupUi()
            self.ui.show()
        except:
            QMessageBox.information(self, 'System', 'An error occurred while opening predict. Please try again!',
                                    QMessageBox.Close)

    def update_profile(self):
        try:
            self.ui = QMainWindow()
            self.ui = profile_user.UI_profile()
            self.ui.setupUi()
            self.ui.show()
            id = self.label_id.text()
            data_user = connect_database.select_user_by_id(id)
            self.ui.txt_name.setText(str(data_user[0][0]))
            self.ui.txt_name_2.setText(str(data_user[0][1]))
            self.ui.txt_name_3.setText(str(data_user[0][3]))
            self.ui.txt_name_4.setText(str(data_user[0][4]))
            self.ui.txt_name_5.setText(str(data_user[0][5]))
            self.ui.txt_name_6.setText(str(data_user[0][6]))
            self.ui.txt_name_7.setText(str(data_user[0][7]))
            self.ui.dateEdit.setDate(data_user[0][2])
            pixmap = QPixmap()
            pixmap.loadFromData(data_user[0,9])
            self.ui.label.setPixmap(QtGui.QPixmap(pixmap))
        except:
            QMessageBox.information(self, 'System', 'There was an error show profile. Please try again later!',
                                    QMessageBox.Close)

    def sign_out(self):
        try:
            name = self.label_3.text()
            ques = QMessageBox.question(self, 'System', f'Are you sure you want to sign out? {name}',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ques == QMessageBox.Yes:
                self.hide()
                self.ui = QMainWindow()
                self.ui = login_3.UI_login_3()
                self.ui.setupUi()
                self.ui.show()
            else:
                pass
        except Exception as err:
            QMessageBox.information(self, 'System', 'An error occurred while logging out. Please try again later!\n'
                                                    f'{str(err)}',
                                    QMessageBox.Close)

    def about_us(self):
        pass

    def closeEvent(self, event):
        try:
            ques = QMessageBox.question(self, 'Close System', 'Are you sure you want to exit system?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ques == QMessageBox.Yes:
                self.hide()
                self.ui = QMainWindow()
                self.ui = login_3.UI_login_3()
                self.ui.setupUi()
                self.ui.show()
            else:
                event.ignore()
        except:
            QMessageBox.information(self, 'System', 'An error occurred while closing. Please try again!',
                                    QMessageBox.Close)
    def view(self):
        try:
            graph = self.cbo_data.currentText()
            path_file = self.label_storage_link.text()
            if graph == 'Percentage of Student Target':
                machine_learning.percentage_of_student_target(path_file,'show')
            if graph == 'Number of student target by Genders':
                machine_learning.number_of_student_target_by_genders(path_file,'show')
            if graph == 'Number of student target by Marital Status':
                machine_learning.number_of_student_target_by_arital_status(path_file,'show')
            if graph == 'Number of student enrolled by Ages':
                machine_learning.number_of_student_enrolled_by_ages(path_file,'show')
            if graph == 'Dropout percentage by Ages':
                machine_learning.dropout_percentage_by_ges(path_file,'show')
            if graph == 'Number of student with Educational Special Needs':
                machine_learning.number_of_student_with_educational_special_needs(path_file,'show')
            if graph == 'Statistics/comparison in Number of student Target by Debt':
                machine_learning.statistics_comparison_in_number_of_studen_target_by_debt(path_file,'show')
            if graph == 'Rate of Unemployment student':
                machine_learning.rate_of_unemployment_student(path_file,'show')
            if graph == 'Correlation heatmap between variables':
                machine_learning.correlation_heatmap_between_variables(path_file,'show')
            # if graph == 'Assess the accuracy of the model through the confusion matrix scale':
            #     print('chua xong doi phan tich not may cai o tren da !!!!!!!!!!!!!')
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while displaying the chart. Please try again later!',
                                    QMessageBox.Close)

    def train(self):
        try:
            list_32_col = ['Marital status', 'Application mode', 'Application order', 'Course',
                           'Daytime/evening attendance',
                           'Previous qualification', 'Mother\'s qualification',
                           'Father\'s qualification', 'Mother\'s occupation',
                           'Father\'s occupation', 'Displaced', 'Educational special needs', 'Debtor',
                           'Tuition fees up to date', 'Gender', 'Scholarship holder', 'Age at enrollment',
                           'Curricular units 1st sem (credited)', 'Curricular units 1st sem (enrolled)',
                           'Curricular units 1st sem (evaluations)', 'Curricular units 1st sem (grade)',
                           'Curricular units 1st sem (approved)',
                           'Curricular units 1st sem (without evaluations)', 'Curricular units 2nd sem (credited)',
                           'Curricular units 2nd sem (evaluations)', 'Curricular units 2nd sem (enrolled)',
                           'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)',
                           'Curricular units 2nd sem (approved)',
                           'Unemployment rate', 'Inflation rate', 'GDP']
            algorithm = self.comboBox.currentText()
            self.progressBar.show()
            n = 100
            for i in range(n):
                time.sleep(0.01)
                self.progressBar.setValue(i + 1)
            self.progressBar.hide()
            self.btn_pridict.setEnabled(True)
            path_file = self.label_storage_link.text()

            if algorithm == 'Logistic Regression':
                self.ui = QMainWindow()
                self.ui = logistic_regression.UI_logistic_regression()
                self.ui.setupUi()
                self.ui.columns.addItems(list_32_col)
                self.ui.label_link.setText(path_file)
                self.ui.show()
            elif algorithm == 'Random Forest Classifier':
                self.ui = QMainWindow()
                self.ui = random_forest.UI_random_forest()
                self.ui.setupUi()
                self.ui.columns.addItems(list_32_col)
                self.ui.label_link.setText(path_file)
                self.ui.show()
            elif algorithm == 'Linear Regression':
                self.ui = QMainWindow()
                self.ui = linear_regression.UI_linear_regression()
                self.ui.setupUi()
                self.ui.columns.addItems(list_32_col)
                self.ui.label_link.setText(path_file)
                self.ui.number_col.setText('32')
                self.ui.show()
            elif algorithm == 'K-Nearest Neighbors Classifier':
                self.ui = QMainWindow()
                self.ui = knn.UI_knn()
                self.ui.setupUi()
                self.ui.columns.addItems(list_32_col)
                self.ui.label_link.setText(path_file)
                # self.ui.number_col.setText('32')
                self.ui.show()
            else:
                self.ui = QMainWindow()
                self.ui = decision_tree.UI_decision_tree()
                self.ui.setupUi()
                self.ui.columns.addItems(list_32_col)
                self.ui.label_link.setText(path_file)
                self.ui.number_col.setText('32')
                self.ui.show()
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while training the model. Please try again later!',
                                    QMessageBox.Close)

    def pridict(self):
        try:
            algorithm = self.comboBox.currentText()
            print(algorithm)
            self.ui = QMainWindow()
            self.ui = predict.Ui_predict_window()
            self.ui.setupUi()
            self.ui.show()
            self.ui.label_link.setText(self.label_storage_link.text())
            self.ui.label_tt.setText(algorithm)
        except:
            QMessageBox.information(self, 'System', 'An error occurred while opening predict. Please try again!',
                                    QMessageBox.Close)

    def corr(self):
        try:
            text_combo_corr = self.comboBox_2.currentText()
            text_label_cols = self.label_8.text()
            list_cols = text_label_cols.split(', ')
            list_32_col = ['Marital status', 'Application mode', 'Application order', 'Course',
                           'Daytime/evening attendance',
                           'Previous qualification', 'Mother\'s qualification',
                           'Father\'s qualification', 'Mother\'s occupation',
                           'Father\'s occupation', 'Displaced', 'Educational special needs', 'Debtor',
                           'Tuition fees up to date', 'Gender', 'Scholarship holder', 'Age at enrollment',
                           'Curricular units 1st sem (credited)', 'Curricular units 1st sem (enrolled)',
                           'Curricular units 1st sem (evaluations)', 'Curricular units 1st sem (grade)',
                           'Curricular units 1st sem (approved)',
                           'Curricular units 1st sem (without evaluations)', 'Curricular units 2nd sem (credited)',
                           'Curricular units 2nd sem (evaluations)', 'Curricular units 2nd sem (enrolled)',
                           'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)',
                           'Curricular units 2nd sem (approved)',
                           'Unemployment rate', 'Inflation rate', 'GDP']
            self.label_10.setText('')
            if text_combo_corr in list_32_col:
                if self.check(list_cols, text_combo_corr):
                    self.label_10.setText(text_combo_corr + ', đã chọn rồi!')
                else:
                    if text_label_cols == '':
                        self.label_8.setText(''.join([text_label_cols, text_combo_corr]))
                    else:
                        self.label_8.setText(', '.join([text_label_cols, text_combo_corr]))
            else:
                self.label_10.setText('The data there is no column: ' + text_combo_corr)
        except:
            QMessageBox.information(self, 'System', 'There was an error displaying the chart. Please try again later!',
                                    QMessageBox.Close)

    def check(self, list, txt):
        for i in list:
            if txt == i:
                return True
        return False

    def clear(self, event):
        self.label_8.setText('')

    def view_corr(self):
        try:
            path_file = self.label_storage_link.text()
            text_label_cols = self.label_8.text()
            list_cols = text_label_cols.split(', ')
            if text_label_cols == '':
                QMessageBox.information(self, 'System', 'Please select at least 1 column!', QMessageBox.Close)
            else:
                machine_learning.corr_col(path_file, list_cols)
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while displaying the chart. Please try again later!',
                                    QMessageBox.Close)

    def percentage(self, event):
        try:
            path_file = self.label_storage_link.text()
            self.ui = QMainWindow()
            self.ui = percentage.UI_percentage()
            self.ui.setupUi()
            self.ui.show()
            p_random = machine_learning.random_forest(path_file, ' ', 10, 0.1)
            p_logic = machine_learning.logic_regression(path_file, ' ', 0.1)
            p_liner = machine_learning.liner(path_file, ' ', 0.1)
            p_tree = machine_learning.decision_tree(path_file, ' ', 0.1,10)
            p_knn = machine_learning.knn(path_file, ' ', 0.1, 5)
            self.ui.label_random.setText(str(round(p_random * 100, 8)))
            self.ui.label_logic.setText(str(round(p_logic * 100, 8)))
            self.ui.label_liner.setText(str(round(p_liner * 100, 8)))
            self.ui.label_decision.setText(str(round(p_tree * 100, 8)))
            self.ui.label_knn.setText(str(round(p_knn * 100, 8)))
            dict = {'Random Forest Classifier': p_random,
                    'Logistic Regression': p_logic,
                    'Linear Regression': p_liner,
                    'Decision Tree Classifier': p_tree,
                    'K-Nearest Neighbors Classifier': p_knn,
                    }
            max_percen = max(dict, key=dict.get)
            self.ui.label_tt.setText(max_percen)
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while displaying the percentage. Please try again later!',
                                    QMessageBox.Close)

    def download(self,event):
        try:
            url = "https://drive.google.com/drive/folders/1mRvYDje3WdEU4m-YNHkWP7rTeazrSTS_?usp=share_link"
            gdown.download_folder(url, quiet=True, use_cookies=False)
            QMessageBox.information(self, 'Download', 'Download successfully', QMessageBox.Close)

        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while download . Please try again later!',
                                    QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_import_window()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
