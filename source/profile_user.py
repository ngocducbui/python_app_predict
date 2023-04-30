from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QStyledItemDelegate, QAction, QLineEdit
import sys
from database import connect_database
from source import change_pass
import common as cm
from source import profile_user

class UI_profile(QMainWindow):
    def __init__(self, parent=None):
        super(UI_profile, self).__init__(parent)
        # self.database_config_obj = None

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(651, 643)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowIcon(QtGui.QIcon("../icon/logo.png"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 10, 311, 271))
       # self.label.setStyleSheet("border-image: url(../images/download.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setReadOnly(True)
        self.txt_name.setGeometry(QtCore.QRect(110, 170, 181, 41))
        self.txt_name.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                    "color:rgba(0, 0, 0, 240);\n"
                                    "padding-bottom:7px")
        self.txt_name.setPlaceholderText("")
        self.txt_name.setObjectName("txt_name")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 70, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(11, 34, 57);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_name_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_2.setGeometry(QtCore.QRect(110, 230, 181, 41))
        self.txt_name_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px")
        self.txt_name_2.setPlaceholderText("")
        self.txt_name_2.setObjectName("txt_name_2")
        self.txt_name_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_3.setGeometry(QtCore.QRect(110, 300, 181, 41))
        self.txt_name_3.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px")
        self.txt_name_3.setPlaceholderText("")
        self.txt_name_3.setObjectName("txt_name_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 310, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(430, 300, 181, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txt_name_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_4.setGeometry(QtCore.QRect(430, 360, 181, 41))
        self.txt_name_4.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px")
        self.txt_name_4.setPlaceholderText("")
        self.txt_name_4.setObjectName("txt_name_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 370, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txt_name_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_5.setGeometry(QtCore.QRect(110, 360, 181, 41))
        self.txt_name_5.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px")
        self.txt_name_5.setText("")
        self.txt_name_5.setPlaceholderText("")
        self.txt_name_5.setObjectName("txt_name_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 370, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txt_name_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_6.setGeometry(QtCore.QRect(110, 430, 181, 41))
        self.txt_name_6.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px")
        self.txt_name_6.setText("")
        self.txt_name_6.setPlaceholderText("")
        self.txt_name_6.setObjectName("txt_name_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 440, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.txt_name_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name_7.setEchoMode(QLineEdit.Password)
        self.txt_name_7.setReadOnly(True)
        self.txt_name_7.setGeometry(QtCore.QRect(430, 430, 181, 41))
        self.txt_name_7.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                      "color:rgba(0, 0, 0, 240);\n"
                                      "padding-bottom:7px")
        self.txt_name_7.setText("")
        self.txt_name_7.setPlaceholderText("")
        self.txt_name_7.setObjectName("txt_name_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(320, 440, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.save)
        self.pushButton.setGeometry(QtCore.QRect(250, 530, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
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
            "}\n"
            "\n"
            "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    color:rgba(91, 88, 53, 255);\n"
            "}</string>\n"
            "   </property>\n"
            "   <property name=\"text\">\n"
            "    <string>SIGN IN</string>\n"
            "   </property>\n"
            "  </widget>\n"
            " </widget>\n"
            " <resources/>\n"
            "</ui>\n"
            "")
        self.pushButton.setObjectName("pushButton")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setStyleSheet("text-decoration:underline;\n"
                                    "color: blue")
        self.label_11.mousePressEvent = self.change_password
        self.label_11.setGeometry(QtCore.QRect(470, 480, 181, 16))
        self.label_11.setObjectName("label_11")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton_2.setStyleSheet("background-color:rgb(218, 91, 11)")
        self.pushButton_2.setGeometry(QtCore.QRect(400, 540, 89, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Profile"))
        self.label_3.setText(_translate("MainWindow", "PROFILE "))
        self.label_2.setText(_translate("MainWindow", "ID:"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Date of Birth:"))
        self.label_6.setText(_translate("MainWindow", "Phone:"))
        self.label_7.setText(_translate("MainWindow", "Email:"))
        self.label_8.setText(_translate("MainWindow", "Address:"))
        self.label_9.setText(_translate("MainWindow", "User name:"))
        self.label_10.setText(_translate("MainWindow", "Password:"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.label_11.setText(_translate("MainWindow", "You want to change password?"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))

    def change_password(self, event):
        try:
            cur_pass = self.txt_name_7.text()
            self.ui = QMainWindow()
            self.ui = change_pass.UI_change_password()
            self.ui.setupUi()
            self.ui.show()
            self.ui.current_pass.setText(cur_pass)
            self.ui.label_id_change_pass.setText(self.txt_name.text())
            self.ui.label_old_pass.setText(cur_pass)
            self.hide()
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while opening change password. Please try again!',
                                    QMessageBox.Close)
    def save(self):
        try:
            id = self.txt_name.text()
            name = self.txt_name_2.text()
            phone = self.txt_name_3.text()
            email = self.txt_name_4.text()
            address = self.txt_name_5.text()
            username = self.txt_name_6.text()
            password = self.txt_name_7.text()
            dob = self.dateEdit.date().toPyDate()
            date_now = datetime.now().date()

            # print(id,name,phone,email,address,username,password,dob)
            # id, name, phone, email, address, username, password, dob

            if all(v != '' for v in [name, dob, phone, email, address, username, password]):
                if dob < date_now:
                    if cm.check_phone(phone):
                        if cm.check_email(email):
                            try:
                                if connect_database.update_profile(id, name, phone, email, address, username, password,
                                                                   dob):
                                    QMessageBox.information(self, 'Update profile', 'Update successfully',
                                                            QMessageBox.Close)
                                    self.hide()
                                    self.ui = QMainWindow()
                                    self.ui = profile_user.UI_profile()
                                    self.ui.setupUi()
                                    self.ui.show()
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
                                    pixmap.loadFromData(data_user[0, 9])
                                    self.ui.label.setPixmap(QtGui.QPixmap(pixmap))
                            except:
                                QMessageBox.information(self, 'Update profile', 'Change information failed', QMessageBox.Close)
                        else:
                            QMessageBox.information(self, 'Update profile', 'Wrong email address format!', QMessageBox.Close)
                    else:
                        QMessageBox.information(self, 'Update profile', 'Wrong phone number format!', QMessageBox.Close)
                else:
                    QMessageBox.information(self, 'Update profile', 'Date of birth cannot be greater than current date!', QMessageBox.Close)
            else:
                QMessageBox.information(self, 'Update profile', 'Please fill in all fields!', QMessageBox.Close)
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while changing profile. Please try again!',
                                    QMessageBox.Close)
    def closeEvent(self, event):
        try:
            ques = QMessageBox.question(self, 'Close System', 'Are you sure you want to exit profile?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ques == QMessageBox.Yes:
                self.hide()
            else:
                event.ignore()
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while closing. Please try again later!',
                                    QMessageBox.Close)

    def cancel(self):
        try:
            ques = QMessageBox.question(self, 'Close System', 'Are you sure you want to exit profile?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ques == QMessageBox.Yes:
                self.hide()
            else:
                pass
        except:
            QMessageBox.information(self, 'System',
                                    'Error system. Please try again!',
                                    QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_profile()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
