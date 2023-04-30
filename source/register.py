from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QStyledItemDelegate, QAction, QLineEdit
import sys
from database import connect_database
import common as cm
from source import login_3
from source import profile_user


class UI_register(QMainWindow):
    def __init__(self, parent=None):
        super(UI_register, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(603, 633)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowIcon(QtGui.QIcon("../icon/logo.png"))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 190, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 250, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 370, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 430, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(240, 60, 301, 31))
        self.txt_name.setObjectName("txt_name")
        self.txt_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_phone.setGeometry(QtCore.QRect(240, 180, 301, 31))
        self.txt_phone.setObjectName("txt_phone")
        self.txt_email = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_email.setGeometry(QtCore.QRect(240, 240, 301, 31))
        self.txt_email.setObjectName("txt_email")
        self.tx_username = QtWidgets.QLineEdit(self.centralwidget)
        self.tx_username.setGeometry(QtCore.QRect(240, 360, 301, 31))
        self.tx_username.setObjectName("tx_username")
        self.txt_password = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setGeometry(QtCore.QRect(240, 420, 301, 31))
        self.txt_password.setObjectName("txt_password")
        self.date = QtWidgets.QDateEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(240, 120, 201, 31))
        self.date.setObjectName("date")
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.btn_ok.clicked.connect(self.ok)
        self.btn_ok.setGeometry(QtCore.QRect(120, 580, 89, 31))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_canncel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_canncel.setStyleSheet("background-color:rgb(218, 91, 11)")
        self.btn_canncel.clicked.connect(self.cancel)
        self.btn_canncel.setGeometry(QtCore.QRect(330, 580, 89, 31))
        self.btn_canncel.setObjectName("btn_canncel")
        self.check_box_agree = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box_agree.setGeometry(QtCore.QRect(210, 520, 251, 20))
        self.check_box_agree.setObjectName("check_box_agree")
        self.txt_email_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_email_2.setGeometry(QtCore.QRect(240, 300, 301, 31))
        self.txt_email_2.setText("")
        self.txt_email_2.setObjectName("txt_email_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 310, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(70, 490, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.txt_password_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_password_2.setEchoMode(QLineEdit.Password)
        self.txt_password_2.setGeometry(QtCore.QRect(240, 480, 301, 31))
        self.txt_password_2.setObjectName("txt_password_2")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 25))
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
        self.label_4.setText(_translate("MainWindow", "REGISTER"))
        self.label_5.setText(_translate("MainWindow", "Name:"))
        self.label_6.setText(_translate("MainWindow", "Date of Birth:"))
        self.label_7.setText(_translate("MainWindow", "Phone:"))
        self.label_8.setText(_translate("MainWindow", "Email:"))
        self.label_9.setText(_translate("MainWindow", "Username:"))
        self.label_10.setText(_translate("MainWindow", "Password:"))
        self.btn_ok.setText(_translate("MainWindow", "Register"))
        self.btn_canncel.setText(_translate("MainWindow", "Cancel"))
        self.check_box_agree.setText(_translate("MainWindow", "I agree to the Terms and Conditions"))
        self.label_11.setText(_translate("MainWindow", "Address:"))
        self.label_12.setText(_translate("MainWindow", "Retype Password:"))

    def ok(self):
        try:
            name = self.txt_name.text()
            dob = self.date.dateTime().toPyDateTime().date()
            phone = self.txt_phone.text()
            email = self.txt_email.text()
            address = self.txt_email_2.text()
            username = self.tx_username.text()
            password = self.txt_password.text()
            repassword = self.txt_password_2.text()
            date_now = datetime.now().date()
            role=str(0)
            if all(v != '' for v in [name, dob, phone, email, address, username, password]):
                if repassword == password:
                    if dob < date_now:
                        if cm.check_phone(phone):
                            if cm.check_email(email):
                                try:
                                    if self.check_box_agree.isChecked():
                                        if connect_database.register(name, dob, phone, email, address, username,
                                                                     password, role):
                                            QMessageBox.information(self, 'Register',
                                                                    f'Successful registration. Congratulations {name}',
                                                                    QMessageBox.Close)
                                            self.hide()
                                            self.ui = QMainWindow()
                                            self.ui = login_3.UI_login_3()
                                            self.ui.setupUi()
                                            self.ui.show()
                                        else:
                                            QMessageBox.information(self, 'Register', 'Username already exists',
                                                                    QMessageBox.Close)
                                            # data_user = connect_database.select_user_by_id(id)
                                            # self.ui.txt_name.setText(str(data_user[0][0]))
                                            # self.ui.txt_name_2.setText(str(data_user[0][1]))
                                            # self.ui.txt_name_3.setText(str(data_user[0][3]))
                                            # self.ui.txt_name_4.setText(str(data_user[0][4]))
                                            # self.ui.txt_name_5.setText(str(data_user[0][5]))
                                            # self.ui.txt_name_6.setText(str(data_user[0][6]))
                                            # self.ui.txt_name_7.setText(str(data_user[0][7]))
                                            # self.ui.dateEdit.setDate(data_user[0][2])
                                    else:
                                        QMessageBox.information(self, 'Register', 'Please click the agree button',
                                                                QMessageBox.Close)
                                except:
                                    QMessageBox.information(self, 'Register', 'Register failed!',
                                                            QMessageBox.Close)
                            else:
                                QMessageBox.information(self, 'Register', 'Wrong email address format!',
                                                        QMessageBox.Close)
                        else:
                            QMessageBox.information(self, 'Register', 'Wrong phone number format!', QMessageBox.Close)
                    else:
                        QMessageBox.information(self, 'Register', 'Date of birth cannot be greater than current date!',
                                                QMessageBox.Close)
                else:
                    QMessageBox.information(self, 'Register', 'Passwords do not match!', QMessageBox.Close)
            else:
                QMessageBox.information(self, 'Register', 'Please fill in all fields!', QMessageBox.Close)
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while registering. Please try again later!',
                                    QMessageBox.Close)

    def cancel(self):
        try:
            ques = QMessageBox.question(self, 'Close System', 'Are you sure you want to exit register new user?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ques == QMessageBox.Yes:
                self.hide()
                self.ui = QMainWindow()
                self.ui = login_3.UI_login_3()
                self.ui.setupUi()
                self.ui.show()
            else:
                pass
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while closing. Please try again later!',
                                    QMessageBox.Close)

    def closeEvent(self, event):
        try:
            ques = QMessageBox.question(self, 'Close System', 'Are you sure you want to exit register new user?',
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
            QMessageBox.information(self, 'System',
                                    'An error occurred while closing. Please try again later!',
                                    QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_register()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
