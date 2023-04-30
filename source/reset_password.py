import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QStyledItemDelegate, QAction
import sys
from database import connect_database
import common as cm
from source import login_3
class UI_reset_password(QMainWindow):
    def __init__(self, parent=None):
        super(UI_reset_password, self).__init__(parent)
        # self.database_config_obj = None

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(529, 469)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowIcon(QtGui.QIcon("../icon/logo.png"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_username = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_username.setGeometry(QtCore.QRect(190, 160, 271, 31))
        self.txt_username.setObjectName("txt_username")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 170, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_phone.setGeometry(QtCore.QRect(190, 230, 271, 31))
        self.txt_phone.setObjectName("txt_phone")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 240, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 310, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_email = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_email.setGeometry(QtCore.QRect(190, 300, 271, 31))
        self.txt_email.setObjectName("txt_email")
        self.txt_name_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_4.setGeometry(QtCore.QRect(190, 90, 271, 31))
        self.txt_name_4.setObjectName("txt_name_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 100, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_reset.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.btn_reset.setGeometry(QtCore.QRect(150, 380, 111, 31))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_canncel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_canncel.setStyleSheet("background-color:rgb(218, 91, 11)")
        self.btn_canncel.clicked.connect(self.cancel)
        self.btn_canncel.setGeometry(QtCore.QRect(320, 380, 89, 31))
        self.btn_canncel.setObjectName("btn_canncel")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "FORGET PASSWORD"))
        self.label.setText(_translate("MainWindow", "Username:"))
        self.label_2.setText(_translate("MainWindow", "Phone:"))
        self.label_4.setText(_translate("MainWindow", "Email:"))
        self.label_5.setText(_translate("MainWindow", "Name:"))
        self.btn_reset.setText(_translate("MainWindow", "Reset Password"))
        self.btn_canncel.setText(_translate("MainWindow", "Cancel"))

    def reset(self):
        try:
            name = self.txt_name_4.text()
            username = self.txt_username.text()
            phone = self.txt_phone.text()
            email = self.txt_email.text()
            new_pass=cm.random_password()
            if all(v != '' for v in [name, username, phone, email]):
                try:
                    a = connect_database.select_id_to_reset_password(name, username, phone, email)
                    if len(a) != 0:
                        if connect_database.reset_password(a[0][0],new_pass):
                            QMessageBox.information(self, 'Reset password', f'Password reset successful: {new_pass}',
                                                    QMessageBox.Close)
                            self.hide()
                            self.ui = QMainWindow()
                            self.ui = login_3.UI_login()
                            self.ui.setupUi()
                            self.ui.show()
                        else:
                            QMessageBox.information(self, 'Reset password', 'Password reset failed!', QMessageBox.Close)

                    else:
                        QMessageBox.information(self, 'Reset password', 'You entered the wrong information!', QMessageBox.Close)
                except:
                    QMessageBox.information(self, 'Login', 'Password reset failed!', QMessageBox.Close)
            else:
                QMessageBox.information(self, 'Login', 'Please enter all data fields!', QMessageBox.Close)
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while resetting password. Please try again later!',
                                    QMessageBox.Close)

    def closeEvent(self, event):
        try:
            self.ui = QMainWindow()
            self.ui = login_3.UI_login_3()
            self.ui.setupUi()
            self.ui.show()
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while closing. Please try again later!',
                                    QMessageBox.Close)
    def cancel(self):
        try:
            self.hide()
            self.ui = QMainWindow()
            self.ui = login_3.UI_login_3()
            self.ui.setupUi()
            self.ui.show()
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while closing. Please try again later!',
                                    QMessageBox.Close)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_reset_password()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
