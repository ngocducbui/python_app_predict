from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QStyledItemDelegate, QAction, QLineEdit
import sys

import machine_learning
from source import predict


class UI_random_forest(QMainWindow):
    def __init__(self, parent=None):
        super(UI_random_forest, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(820, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setWindowIcon(QtGui.QIcon("../icon/logo.png"))
        self.centralwidget.setObjectName("centralwidget")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(360, 80, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 270, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 330, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.mse = QtWidgets.QLabel(self.centralwidget)
        self.mse.setStyleSheet("color:red")
        self.mse.setGeometry(QtCore.QRect(580, 110, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.mse.setFont(font)
        self.mse.setObjectName("mse")
        self.test_data = QtWidgets.QLineEdit(self.centralwidget)
        self.test_data.setGeometry(QtCore.QRect(150, 300, 81, 23))
        self.test_data.setObjectName("test_data")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(30, 390, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.mae = QtWidgets.QLabel(self.centralwidget)
        self.mae.setGeometry(QtCore.QRect(580, 80, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.mae.setFont(font)
        self.mae.setStyleSheet("color:red")

        self.mae.setObjectName("mae")
        self.test_size = QtWidgets.QLabel(self.centralwidget)
        self.test_size.setGeometry(QtCore.QRect(150, 360, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.test_size.setFont(font)
        self.test_size.setText("")
        self.test_size.setObjectName("test_size")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(330, 50, 20, 561))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setGeometry(QtCore.QRect(80, 530, 111, 41))
        self.train.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.train.clicked.connect(self.train_random)
        self.train.setIcon(QtGui.QIcon('../icon/training.png'))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.train.setFont(font)
        self.train.setObjectName("train")
        self.columns = QtWidgets.QListWidget(self.centralwidget)
        self.columns.setGeometry(QtCore.QRect(30, 50, 291, 191))
        self.columns.setObjectName("columns")
        self.rmse = QtWidgets.QLabel(self.centralwidget)
        self.rmse.setStyleSheet("color:red")

        self.rmse.setGeometry(QtCore.QRect(580, 140, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.rmse.setFont(font)
        self.rmse.setObjectName("rmse")
        self.train_size = QtWidgets.QLabel(self.centralwidget)
        self.train_size.setGeometry(QtCore.QRect(150, 330, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.train_size.setFont(font)
        self.train_size.setText("")
        self.train_size.setObjectName("train_size")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(360, 110, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(360, 170, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(360, 140, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.accuracy = QtWidgets.QLabel(self.centralwidget)
        self.accuracy.setStyleSheet("color:red")
        self.accuracy.setGeometry(QtCore.QRect(580, 170, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.accuracy.setFont(font)
        self.accuracy.setObjectName("accuracy")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 360, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.conf_mat = QtWidgets.QPushButton(self.centralwidget)
        self.conf_mat.clicked.connect(self.con_matrix)
        self.conf_mat.setEnabled(False)
        self.conf_mat.setGeometry(QtCore.QRect(370, 480, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.conf_mat.setFont(font)
        self.conf_mat.setObjectName("conf_mat")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 300, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.test_size_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_size_btn.setGeometry(QtCore.QRect(260, 300, 71, 23))
        self.test_size_btn.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.test_size_btn.clicked.connect(self.set_size)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.test_size_btn.setFont(font)
        self.test_size_btn.setObjectName("test_size_btn")
        self.max_depth = QtWidgets.QLineEdit(self.centralwidget)
        self.max_depth.setGeometry(QtCore.QRect(150, 390, 171, 23))
        self.max_depth.setText("")
        self.max_depth.setObjectName("max_depth")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(360, 210, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.report = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(360, 240, 441, 211))
        self.report.setObjectName("report")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.report.setFont(font)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, -10, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(11, 34, 57);")
        self.label_4.setObjectName("label_4")
        self.target_2 = QtWidgets.QLabel(self.centralwidget)
        self.target_2.setGeometry(QtCore.QRect(150, 270, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.target_2.setFont(font)
        self.target_2.setObjectName("target_2")
        self.train_2 = QtWidgets.QPushButton(self.centralwidget)
        self.train_2.clicked.connect(self.predict_open)
        self.train_2.setIcon(QtGui.QIcon('../icon/prediction.png'))
        self.train_2.setEnabled(False)
        self.train_2.setGeometry(QtCore.QRect(540, 530, 111, 41))
        self.train_2.setStyleSheet("background-color:rgb(94, 186, 125)")
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.train_2.setFont(font)
        self.train_2.setObjectName("train_2")
        self.label_link = QtWidgets.QLabel(self.centralwidget)
        self.label_link.hide()
        self.label_link.setGeometry(QtCore.QRect(590, 20, 55, 16))
        self.label_link.setObjectName("label_link")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Ramdom Forest"))
        self.label_13.setText(_translate("MainWindow", "Mean Absolute Error:"))
        self.label_11.setText(_translate("MainWindow", "Target : "))
        self.label_10.setText(_translate("MainWindow", "Train Size"))
        self.mse.setText(_translate("MainWindow", ""))
        self.test_data.setText(_translate("MainWindow", "0.1"))
        self.label_20.setText(_translate("MainWindow", "Max_depth:"))
        self.mae.setText(_translate("MainWindow", ""))
        self.train.setText(_translate("MainWindow", "Train"))
        self.rmse.setText(_translate("MainWindow", ""))
        self.label_15.setText(_translate("MainWindow", "Mean Square Error:"))
        self.label_24.setText(_translate("MainWindow", "Accuracy Score:"))
        self.label_14.setText(_translate("MainWindow", "Root Mean Sq. Error:"))
        self.accuracy.setText(_translate("MainWindow", ""))
        self.label_9.setText(_translate("MainWindow", "Test Size"))
        self.conf_mat.setText(_translate("MainWindow", "Confusion Matrix"))
        self.label_12.setText(_translate("MainWindow", "Test Data Size:"))
        self.test_size_btn.setText(_translate("MainWindow", "Set"))
        self.max_depth.setPlaceholderText(_translate("MainWindow", "Number of max_depth"))
        self.label_25.setText(_translate("MainWindow", "Classification Report:"))
        self.label_4.setText(_translate("MainWindow", "Random Forest"))
        self.target_2.setText(
            _translate("MainWindow", "<html><head/><body><p>Dropout or Graduate<br/></p></body></html>"))
        self.train_2.setText(_translate("MainWindow", "Predict"))
        self.label_link.setText(_translate("MainWindow", "TextLabel"))

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

    def train_random(self):
        try:
            number = self.test_data.text()
            path = self.label_link.text()
            max_depth = self.max_depth.text()
            result = machine_learning.random_forest(path, 'error', int(max_depth), float(number))
            self.mae.setText(str(result[0]))
            self.mse.setText(str(result[1]))
            self.rmse.setText(str(result[2]))
            self.accuracy.setText(str(result[3]))
            self.report.setPlainText(str(result[4]))
        except:
            QMessageBox.information(self, 'System', 'An error occurred while training. Please try again!',
                                    QMessageBox.Close)
        else:
            self.train_2.setEnabled(True)
            self.conf_mat.setEnabled(True)

    def con_matrix(self):
        try:
            number = self.test_data.text()
            max_depth = self.max_depth.text()
            path = self.label_link.text()
            machine_learning.random_forest(path, 'matrix', int(max_depth), float(number))
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while displaying the confusion matrix. Please try again!',
                                    QMessageBox.Close)

    def predict_open(self):
        try:
            number = self.test_data.text()
            max_depth = self.max_depth.text()
            self.ui = QMainWindow()
            self.ui = predict.Ui_predict_window(max_depth,number)
            self.ui.setupUi()
            self.ui.label_link.setText(self.label_link.text())
            self.ui.label_tt.setText('Random Forest Classifier')
            self.ui.show()
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while opening predict. Please try again!',
                                    QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_random_forest()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
