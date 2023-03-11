from PyQt5 import QtCore, QtGui, QtWidgets
from HiringWindow import Ui_HiringWindow
from CandidateWindow import Ui_CandidateWindow


class Ui_MainWindow(object):
    def openHiringWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HiringWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCandidateWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CandidateWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1420, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1420, 800))
        self.widget.setStyleSheet(
            "QWidget#widget{background-image:url(C:/Users/user/PycharmProjects/pythonProject/mainbg)}\n"
            "")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(390, 100, 631, 141))
        self.label.setStyleSheet("font: 44pt \"Arial Rounded MT Bold\";\n"
                                 "color: \"cyan\"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.clicked.connect(lambda: [self.openHiringWindow(), MainWindow.hide()])
        self.pushButton.setGeometry(QtCore.QRect(270, 440, 250, 50))
        self.pushButton.setStyleSheet("*{\n"
                                      "    border-radius:10px;\n"
                                      "    font: 18pt \"Arial Rounded MT Bold\";\n"
                                      "    color:rgb(0, 0, 127);\n"
                                      "    background-color:\"cyan\";\n"
                                      "}\n"
                                      "\n"
                                      "*:hover{\n"
                                      "            background: rgb(89, 51, 135)\n"
                                      "        }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.clicked.connect(lambda: [self.openCandidateWindow(), MainWindow.hide()])
        self.pushButton_2.setGeometry(QtCore.QRect(920, 440, 250, 50))
        self.pushButton_2.setStyleSheet("*{\n"
                                        "    border-radius:10px;\n"
                                        "    font: 18pt \"Arial Rounded MT Bold\";\n"
                                        "    color:rgb(0, 0, 127);\n"
                                        "    background-color:\"cyan\";\n"
                                        "}\n"
                                        "\n"
                                        "*:hover{\n"
                                        "            background: rgb(89, 51, 135)\n"
                                        "        }")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RESUME PARSER"))
        self.pushButton.setText(_translate("MainWindow", "Hiring Team"))
        self.pushButton_2.setText(_translate("MainWindow", "Candidate"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
