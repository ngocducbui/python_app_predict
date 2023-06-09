from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QStyledItemDelegate, QAction, QLineEdit
import sys

import machine_learning
from source import predict

from PyQt5 import QtCore, QtGui, QtWidgets


class UI_decision_tree(QMainWindow):
    def __init__(self, parent=None):
        super(UI_decision_tree, self).__init__(parent)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(821, 606)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setWindowIcon(QtGui.QIcon("../icon/logo.png"))
        self.centralwidget.setObjectName("centralwidget")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(190, 10, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(11, 34, 57);")
        self.label_14.setObjectName("label_14")
        self.columns = QtWidgets.QListWidget(self.centralwidget)
        self.columns.setGeometry(QtCore.QRect(20, 90, 301, 191))
        self.columns.setObjectName("columns")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 55, 16))
        self.label.setObjectName("label")
        self.number_col = QtWidgets.QLabel(self.centralwidget)
        self.number_col.setGeometry(QtCore.QRect(90, 70, 91, 16))
        self.number_col.setObjectName("number_col")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 420, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.target_2 = QtWidgets.QLabel(self.centralwidget)
        self.target_2.setGeometry(QtCore.QRect(160, 300, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.target_2.setFont(font)
        self.target_2.setObjectName("target_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 380, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.test_size = QtWidgets.QLabel(self.centralwidget)
        self.test_size.setGeometry(QtCore.QRect(160, 420, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.test_size.setFont(font)
        self.test_size.setObjectName("test_size")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.test_size_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_size_btn.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.test_size_btn.clicked.connect(self.set_size)
        self.test_size_btn.setGeometry(QtCore.QRect(250, 340, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.test_size_btn.setFont(font)
        self.test_size_btn.setObjectName("test_size_btn")
        self.test_data = QtWidgets.QLineEdit(self.centralwidget)
        self.test_data.setGeometry(QtCore.QRect(160, 340, 81, 23))
        self.test_data.setObjectName("test_data")
        self.train_size = QtWidgets.QLabel(self.centralwidget)
        self.train_size.setGeometry(QtCore.QRect(160, 380, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.train_size.setFont(font)
        self.train_size.setObjectName("train_size")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(330, 60, 20, 491))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(360, 170, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(360, 130, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.mse = QtWidgets.QLabel(self.centralwidget)
        self.mse.setStyleSheet("color:red")
        self.mse.setGeometry(QtCore.QRect(570, 130, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.mse.setFont(font)
        self.mse.setObjectName("mse")
        self.mae = QtWidgets.QLabel(self.centralwidget)
        self.mae.setStyleSheet("color:red")
        self.mae.setGeometry(QtCore.QRect(570, 100, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.mae.setFont(font)
        self.mae.setObjectName("mae")
        self.rmse = QtWidgets.QLabel(self.centralwidget)
        self.rmse.setStyleSheet("color:red")

        self.rmse.setGeometry(QtCore.QRect(570, 170, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.rmse.setFont(font)
        self.rmse.setObjectName("rmse")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(360, 100, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(360, 210, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.accuracy = QtWidgets.QLabel(self.centralwidget)
        self.accuracy.setStyleSheet("color:red")
        self.accuracy.setGeometry(QtCore.QRect(570, 210, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.accuracy.setFont(font)
        self.accuracy.setObjectName("accuracy")
        self.report = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.report.setFont(font)
        self.report.setGeometry(QtCore.QRect(360, 270, 451, 201))
        self.report.setObjectName("report")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(360, 240, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.predict_2 = QtWidgets.QPushButton(self.centralwidget)
        self.predict_2.clicked.connect(self.predict_open)
        self.predict_2.setIcon(QtGui.QIcon('../icon/prediction.png'))
        self.predict_2.setEnabled(False)
        self.predict_2.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.predict_2.setGeometry(QtCore.QRect(600, 510, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.predict_2.setFont(font)
        self.predict_2.setObjectName("predict_2")
        self.conf_mat_2 = QtWidgets.QPushButton(self.centralwidget)
        self.conf_mat_2.clicked.connect(self.con_matrix)
        self.conf_mat_2.setEnabled(False)
        self.conf_mat_2.setGeometry(QtCore.QRect(360, 480, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.conf_mat_2.setFont(font)
        self.conf_mat_2.setObjectName("conf_mat_2")
        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setStyleSheet("background-color:rgb(94, 186, 125)")
        self.train.clicked.connect(self.train_tree)
        self.train.setIcon(QtGui.QIcon('../icon/training.png'))
        self.train.setGeometry(QtCore.QRect(200, 510, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.train.setFont(font)
        self.train.setObjectName("train")
        self.label_link = QtWidgets.QLabel(self.centralwidget)
        self.label_link.hide()
        self.label_link.setGeometry(QtCore.QRect(580, 20, 55, 16))
        self.label_link.setObjectName("label_link")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(20, 460, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.max_depth = QtWidgets.QLineEdit(self.centralwidget)
        self.max_depth.setGeometry(QtCore.QRect(160, 460, 171, 23))
        self.max_depth.setText("")
        self.max_depth.setObjectName("max_depth")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Decision Tree"))
        self.label_14.setText(_translate("MainWindow", "Decision Tree Classifier"))
        self.label.setText(_translate("MainWindow", "Columns:"))
        self.number_col.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Target : "))
        self.label_9.setText(_translate("MainWindow", "Test Size:"))
        self.target_2.setText(
            _translate("MainWindow", "<html><head/><body><p>Dropout or Graduate<br/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Train Size:"))
        self.test_size.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow", "Test Data Size:"))
        self.test_size_btn.setText(_translate("MainWindow", "Set"))
        self.test_data.setText(_translate("MainWindow", "0.1"))
        self.train_size.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", "Root Mean Sq. Error:"))
        self.label_12.setText(_translate("MainWindow", "Mean Square Error:"))
        self.mse.setText(_translate("MainWindow", ""))
        self.mae.setText(_translate("MainWindow", ""))
        self.rmse.setText(_translate("MainWindow", ""))
        self.label_11.setText(_translate("MainWindow", "Mean Absolute Error:"))
        self.label_24.setText(_translate("MainWindow", "Accuracy Score:"))
        self.accuracy.setText(_translate("MainWindow", ""))
        self.label_25.setText(_translate("MainWindow", "Classification Report:"))
        self.predict_2.setText(_translate("MainWindow", "Predict"))
        self.conf_mat_2.setText(_translate("MainWindow", "Confusion Matrix"))
        self.train.setText(_translate("MainWindow", "Train"))
        self.label_link.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "Max_depth:"))
        self.max_depth.setPlaceholderText(_translate("MainWindow", "Number of max_depth"))

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

    def train_tree(self):
        try:
            max_depth = self.max_depth.text()
            number = self.test_data.text()
            path = self.label_link.text()
            result = machine_learning.decision_tree(path, 'error', float(number), int(max_depth))
            self.mae.setText(str(result[0]))
            self.mse.setText(str(result[1]))
            self.rmse.setText(str(result[2]))
            self.accuracy.setText(str(result[3]))
            self.report.setPlainText(str(result[4]))
        except:
            QMessageBox.information(self, 'System', 'An error occurred while training. Please try again!',
                                    QMessageBox.Close)
        else:
            self.predict_2.setEnabled(True)
            self.conf_mat_2.setEnabled(True)

    def con_matrix(self):
        try:
            max_depth = self.max_depth.text()
            number = self.test_data.text()
            path = self.label_link.text()
            machine_learning.decision_tree(path, 'matrix', float(number),int(max_depth))
        except Exception as err:
            QMessageBox.information(self, 'System',
                                    'An error occurred while displaying the confusion matrix. Please try again!\n'
                                    f'{str(err)}',
                                    QMessageBox.Close)

    def predict_open(self):
        try:
            max_depth = self.max_depth.text()
            number = self.test_data.text()
            self.ui = QMainWindow()
            self.ui = predict.Ui_predict_window(max_depth,number)
            self.ui.setupUi()
            self.ui.label_link.setText(self.label_link.text())
            self.ui.label_tt.setText('Decision Tree Classifier')
            self.ui.show()
        except:
            QMessageBox.information(self, 'System',
                                    'An error occurred while opening predict. Please try again!',
                                    QMessageBox.Close)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI_decision_tree()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
