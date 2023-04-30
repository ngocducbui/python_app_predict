from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QStyledItemDelegate, QAction, QLineEdit
from database import connect_database
from source import profile_user


class UI_change_password(QMainWindow):
    def __init__(self, parent=None):
        super(UI_change_password, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(459, 503)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setWindowIcon(QtGui.QIcon("../icon/logo.png"))
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 321, 51))
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
        self.label_2.setGeometry(QtCore.QRect(20, 130, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.current_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.current_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.current_pass.setGeometry(QtCore.QRect(170, 120, 261, 41))
        self.current_pass.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                        "border:none;\n"
                                        "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                        "color:rgba(0, 0, 0, 240);\n"
                                        "padding-bottom:7px")
        self.current_pass.setPlaceholderText("")
        self.current_pass.setObjectName("current_pass")
        self.new_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.new_pass.setEchoMode(QLineEdit.Password)
        self.new_pass.setGeometry(QtCore.QRect(170, 200, 261, 41))
        self.new_pass.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                    "color:rgba(0, 0, 0, 240);\n"
                                    "padding-bottom:7px")
        self.new_pass.setText("")
        self.new_pass.setPlaceholderText("")
        self.new_pass.setObjectName("new_pass")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_id_change_pass = QtWidgets.QLabel("Hidden Label", self)
        self.label_id_change_pass.hide()
        self.label_id_change_pass.setGeometry(QtCore.QRect(20, 210, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_id_change_pass.setFont(font)
        self.label_id_change_pass.setObjectName("label_id_change_pass")
        self.re_new_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.re_new_pass.setGeometry(QtCore.QRect(170, 280, 261, 41))
        self.re_new_pass.setEchoMode(QLineEdit.Password)
        self.re_new_pass.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                                       "border:none;\n"
                                       "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                                       "color:rgba(0, 0, 0, 240);\n"
                                       "padding-bottom:7px")
        self.re_new_pass.setText("")
        self.re_new_pass.setPlaceholderText("")
        self.re_new_pass.setObjectName("re_new_pass")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 290, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_old_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_old_pass.hide()
        self.label_old_pass.setGeometry(QtCore.QRect(20, 290, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_old_pass.setFont(font)
        self.label_old_pass.setObjectName("label_old_pass")

        self.btn_change = QtWidgets.QPushButton(self.centralwidget)
        self.btn_change.clicked.connect(self.change_pass)
        self.btn_change.setGeometry(QtCore.QRect(110, 400, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_change.setFont(font)
        self.btn_change.setStyleSheet(
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
        self.btn_change.setObjectName("btn_change")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_cancel.setGeometry(QtCore.QRect(260, 410, 89, 27))
        self.btn_cancel.setObjectName("btn_cancel")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 25))
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
        self.label_3.setText(_translate("MainWindow", "CHANGE PASSWORD"))
        self.label_2.setText(_translate("MainWindow", "Current Password:"))
        self.label_4.setText(_translate("MainWindow", "New Password:"))
        self.label_id_change_pass.setText(_translate("MainWindow", "id can doi password111:"))
        self.label_5.setText(_translate("MainWindow", "Retype Password:"))
        self.label_old_pass.setText(_translate("MainWindow", "label for storage old password"))
        self.btn_change.setText(_translate("MainWindow", "Change"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))

    def change_pass(self):
        try:
            id = self.label_id_change_pass.text()
            curr_pass = self.current_pass.text()
            new_pass = self.new_pass.text()
            re_pass = self.re_new_pass.text()
            old_pass = self.label_old_pass.text()
            if curr_pass == old_pass:
                if new_pass == re_pass:
                    if new_pass != curr_pass:
                        try:
                            if connect_database.change_password(id, re_pass):
                                QMessageBox.information(self, 'Change Password', 'Password change successfully ',
                                                        QMessageBox.Close)
                                self.hide()
                                self.ui = QMainWindow()
                                self.ui = profile_user.UI_profile()
                                self.ui.setupUi()
                                self.ui.show()
                                self.ui.txt_name_7.setText(new_pass)
                                data_user = connect_database.select_user_by_id(id)
                                self.ui.txt_name.setText(str(data_user[0][0]))
                                self.ui.txt_name_2.setText(str(data_user[0][1]))
                                self.ui.txt_name_3.setText(str(data_user[0][3]))
                                self.ui.txt_name_4.setText(str(data_user[0][4]))
                                self.ui.txt_name_5.setText(str(data_user[0][5]))
                                self.ui.txt_name_6.setText(str(data_user[0][6]))
                                self.ui.dateEdit.setDate(data_user[0][2])
                        except:
                            QMessageBox.information(self, 'Change Password', 'Password change failed!',
                                                    QMessageBox.Close)
                    else:
                        QMessageBox.information(self, 'Change Password',
                                                'The new password cannot be the same as the old password!',
                                                QMessageBox.Close)
                else:
                    QMessageBox.information(self, 'Change Password', 'The password does not match!', QMessageBox.Close)
            else:
                QMessageBox.information(self, 'Change Password', 'Current password is not correct!', QMessageBox.Close)
        except:
            QMessageBox.information(self, 'System', 'An error occurred while changing password. Please try again!',
                                    QMessageBox.Close)

    def cancel(self):
        try:
            id = self.label_id_change_pass.text()
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
        except:
            QMessageBox.information(self, 'System', 'An error occurred while closing. Please try again!',
                                    QMessageBox.Close)

    def closeEvent(self, event):
        try:
            ques = QMessageBox.question(self, 'Close System', 'Are you sure you want to exit change password?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ques == QMessageBox.Yes:
                id = self.label_id_change_pass.text()
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
            else:
                event.ignore()
        except:
            QMessageBox.information(self, 'System', 'An error occurred while closing. Please try again!',
                                    QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_change_password()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
