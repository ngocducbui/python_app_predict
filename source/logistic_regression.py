from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QStyledItemDelegate, QAction, QLineEdit
import sys

import machine_learning
from source import predict

class UI_logistic_regression(QMainWindow):
    def __init__(self, parent=None):
        super(UI_logistic_regression, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(850, 633)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setWindowIcon(QtGui.QIcon("../icon/logo.png"))
        self.centralwidget.setObjectName("centralwidget")
        self.columns = QtWidgets.QListWidget(self.centralwidget)
        self.columns.setGeometry(QtCore.QRect(20, 80, 301, 271))
        self.columns.setObjectName("columns")
        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.train.setIcon(QtGui.QIcon('../icon/training.png'))
        self.train.clicked.connect(self.train_logistic)
        self.train.setGeometry(QtCore.QRect(80, 530, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.train.setFont(font)
        self.train.setObjectName("train")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(370, 140, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.target = QtWidgets.QLabel(self.centralwidget)
        self.target.setGeometry(QtCore.QRect(100, 370, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.target.setFont(font)
        self.target.setObjectName("target")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(370, 110, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.conf_mat = QtWidgets.QPushButton(self.centralwidget)
        self.conf_mat.clicked.connect(self.con_matrix)
        self.conf_mat.setEnabled(False)
        self.conf_mat.setGeometry(QtCore.QRect(370, 480, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.conf_mat.setFont(font)
        self.conf_mat.setObjectName("conf_mat")
        self.test_data = QtWidgets.QLineEdit(self.centralwidget)
        self.test_data.setGeometry(QtCore.QRect(140, 410, 101, 23))
        self.test_data.setObjectName("test_data")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 370, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_link = QtWidgets.QLabel(self.centralwidget)
        self.label_link.hide()
        self.label_link.setGeometry(QtCore.QRect(20, 370, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_link.setFont(font)
        self.label_link.setObjectName("label_link")
        self.rmse = QtWidgets.QLabel(self.centralwidget)
        self.rmse.setStyleSheet("color:red")
        self.rmse.setGeometry(QtCore.QRect(550, 140, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.rmse.setFont(font)
        self.rmse.setText("")
        self.rmse.setObjectName("rmse")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(370, 80, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.mae = QtWidgets.QLabel(self.centralwidget)
        self.mae.setStyleSheet("color:red")
        self.mae.setGeometry(QtCore.QRect(550, 80, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.mae.setFont(font)
        self.mae.setText("")
        self.mae.setObjectName("mae")
        self.test_size_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_size_btn.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.test_size_btn.clicked.connect(self.set_size)
        self.test_size_btn.setGeometry(QtCore.QRect(250, 410, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.test_size_btn.setFont(font)
        self.test_size_btn.setObjectName("test_size_btn")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 410, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.mse = QtWidgets.QLabel(self.centralwidget)
        self.mse.setStyleSheet("color:red")
        self.mse.setGeometry(QtCore.QRect(550, 110, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.mse.setFont(font)
        self.mse.setText("")
        self.mse.setObjectName("mse")
        self.accuracy = QtWidgets.QLabel(self.centralwidget)
        self.accuracy.setStyleSheet("color:red")

        self.accuracy.setGeometry(QtCore.QRect(550, 170, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.accuracy.setFont(font)
        self.accuracy.setText("")
        self.accuracy.setObjectName("accuracy")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(370, 170, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.test_size = QtWidgets.QLabel(self.centralwidget)
        self.test_size.setGeometry(QtCore.QRect(110, 490, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.test_size.setFont(font)
        self.test_size.setText("")
        self.test_size.setObjectName("test_size")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 490, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.train_size = QtWidgets.QLabel(self.centralwidget)
        self.train_size.setGeometry(QtCore.QRect(110, 450, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.train_size.setFont(font)
        self.train_size.setText("")
        self.train_size.setObjectName("train_size")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 450, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(370, 220, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.report = QtWidgets.QPlainTextEdit(self.centralwidget)
        # self.report.setFont(12)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.report.setFont(font)
        self.report.setGeometry(QtCore.QRect(370, 250, 451, 221))
        self.report.setObjectName("report")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.report.setFont(font)
        self.predict = QtWidgets.QPushButton(self.centralwidget)
        self.predict.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.predict.setEnabled(False)
        self.predict.clicked.connect(self.predict_open)
        self.predict.setIcon(QtGui.QIcon('../icon/prediction.png'))
        self.predict.setGeometry(QtCore.QRect(540, 530, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.predict.setFont(font)
        self.predict.setObjectName("predict")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 0, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(11, 34, 57);")
        self.label_3.setObjectName("label_3")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 25))
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
        self.train.setText(_translate("MainWindow", "Train"))
        self.label_14.setText(_translate("MainWindow", "Root Mean Sq. Error:"))
        self.target.setText(
            _translate("MainWindow", "<html><head/><body><p>Dropout or Graduate<br/></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "Mean Square Error:"))
        self.conf_mat.setText(_translate("MainWindow", "Confusion Matrix"))
        self.test_data.setText(_translate("MainWindow", "0.1"))
        self.label_11.setText(_translate("MainWindow", "Target : "))
        self.label_link.setText(_translate("MainWindow", "label_linklabel_linklabel_link "))
        self.label_13.setText(_translate("MainWindow", "Mean Absolute Error:"))
        self.test_size_btn.setText(_translate("MainWindow", "Set"))
        self.label_12.setText(_translate("MainWindow", "Test Data Size"))
        self.label_24.setText(_translate("MainWindow", "Accuracy Score:"))
        self.label_9.setText(_translate("MainWindow", "Test Size"))
        self.label_10.setText(_translate("MainWindow", "Train Size"))
        self.label_25.setText(_translate("MainWindow", "Classification Report:"))
        self.predict.setText(_translate("MainWindow", "Predict"))
        self.label_3.setText(_translate("MainWindow", "Logistic Regression"))

    def set_size(self):
        try:
            path = self.label_link.text()
            number = self.test_data.text()
            size = machine_learning.size_split(path, float(number))
            self.train_size.setText(str(size[0]))
            self.test_size.setText(str(size[1]))
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while setting test, train size. Please try again!',
                                    QMessageBox.Close)
    def train_logistic(self):
        try:
            number = self.test_data.text()
            path = self.label_link.text()
            result = machine_learning.logic_regression(path, 'error',float(number))
            self.mae.setText(str(result[0]))
            self.mse.setText(str(result[1]))
            self.rmse.setText(str(result[2]))
            self.accuracy.setText(str(result[3]))
            self.report.setPlainText(str(result[4]))
        except:
            QMessageBox.information(self, 'System', 'An error occurred while training. Please try again!',
                                    QMessageBox.Close)
        else:
            self.predict.setEnabled(True)
            self.conf_mat.setEnabled(True)

    def con_matrix(self):
        try:
            path = self.label_link.text()
            number = self.test_data.text()
            machine_learning.logic_regression(path, 'matrix',float(number))
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while displaying the confusion matrix. Please try again!',
                                    QMessageBox.Close)

    def predict_open(self):
        try:
            number = self.test_data.text()
            self.ui = QMainWindow()
            self.ui = predict.Ui_predict_window(0,number)
            self.ui.setupUi()
            self.ui.label_link.setText(self.label_link.text())
            self.ui.label_tt.setText('Logistic Regression')
            self.ui.show()
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while opening predict. Please try again!',
                                    QMessageBox.Close)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_logistic_regression()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
