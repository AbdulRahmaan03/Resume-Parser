from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import main


class Ui_HiringWindow(object):
    def openMoreInformationWindow(self):
        from MoreInfromation import Ui_MoreInformation
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MoreInformation()
        self.ui.setupUi(self.window)
        self.window.show()

    def openMainWindow(self):
        from MainWindow import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def finish(self):
        exit()

    def result(self):
        x = main.display()
        self.label_3.setText(x)

    def buttonClicked(self, x):
        main.get_file_path(x, ttype)
        # main.start()

    def buttonClicked_2(self, x):
        main.get_file_paths(x, ttype)
        # main.start()

    def setupUi(self, HiringWindow):
        HiringWindow.setObjectName("HiringWindow")
        HiringWindow.resize(1420, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HiringWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HiringWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1420, 800))
        self.widget.setStyleSheet(
            "QWidget#widget{background-image:url(C:/Users/user/PycharmProjects/pythonProject/mainbg)}\n"
            "")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(300, 110, 221, 50))
        self.label.setStyleSheet("color: \"cyan\";\n"
                                 "font: 18pt \"Arial Rounded MT Bold\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(880, 110, 331, 50))
        self.label_2.setStyleSheet("color: \"cyan\";\n"
                                   "font: 18pt \"Arial Rounded MT Bold\";")
        self.label_2.setObjectName("label_2")
        self.options = ('Select File', 'Select Files')
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(290, 200, 231, 31))
        self.comboBox.setStyleSheet("")
        self.comboBox.addItems(self.options)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(290, 240, 231, 31))
        self.pushButton.setStyleSheet("*{\n"
                                      "    border-radius:10px;\n"
                                      "    font: 14pt \"MS Shell Dlg 2\";\n"
                                      "    color:rgb(0, 0, 127);\n"
                                      "    background-color:\"cyan\";\n"
                                      "}\n"
                                      "\n"
                                      "*:hover{\n"
                                      "            background: rgb(89, 51, 135)\n"
                                      "        }")
        self.pushButton.clicked.connect(lambda: [self.typefun(1), self.launchDialog()])
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(940, 200, 231, 31))
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.addItems(self.options)
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(940, 240, 231, 31))
        self.pushButton_2.setStyleSheet("*{\n"
                                        "    border-radius:10px;\n"
                                        "    font: 14pt \"MS Shell Dlg 2\";\n"
                                        "    color:rgb(0, 0, 127);\n"
                                        "    background-color:\"cyan\";\n"
                                        "}\n"
                                        "\n"
                                        "*:hover{\n"
                                        "            background: rgb(89, 51, 135)\n"
                                        "        }")
        self.pushButton_2.clicked.connect(lambda: [self.typefun(2), self.launchDialog_2()])
        self.pushButton_2.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(580, 300, 271, 390))
        self.label_3.setStyleSheet("color: \"cyan\";\n"
                                   "font: 10pt \"Arial Rounded MT Bold\";")
        self.label_3.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 290, 150, 30))
        self.pushButton_3.setStyleSheet("*{\n"
                                        "    border-radius:10px;\n"
                                        "    font: 14pt \"MS Shell Dlg 2\";\n"
                                        "    color:rgb(0, 0, 127);\n"
                                        "    background-color:\"cyan\";\n"
                                        "}\n"
                                        "\n"
                                        "*:hover{\n"
                                        "            background: rgb(89, 51, 135)\n"
                                        "        }")
        self.pushButton_3.clicked.connect(lambda: self.result())
        self.pushButton_3.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 700, 110, 50))
        self.pushButton_4.setStyleSheet("*{\n"
                                        "    border-radius:10px;\n"
                                        "    font: 14pt \"MS Shell Dlg 2\";\n"
                                        "    color:rgb(0, 0, 127);\n"
                                        "    background-color:\"cyan\";\n"
                                        "}\n"
                                        "\n"
                                        "*:hover{\n"
                                        "            background: rgb(89, 51, 135)\n"
                                        "        }")
        self.pushButton_4.clicked.connect(lambda: [self.openMainWindow(), HiringWindow.hide()])
        self.pushButton_4.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(1120, 700, 210, 50))
        self.pushButton_5.setStyleSheet("*{\n"
                                        "    border-radius:10px;\n"
                                        "    font: 14pt \"MS Shell Dlg 2\";\n"
                                        "    color:rgb(0, 0, 127);\n"
                                        "    background-color:\"cyan\";\n"
                                        "}\n"
                                        "\n"
                                        "*:hover{\n"
                                        "            background: rgb(89, 51, 135)\n"
                                        "        }")
        self.pushButton_5.clicked.connect(lambda: [self.openMoreInformationWindow(), HiringWindow.hide()])
        self.pushButton_5.setObjectName("pushButton")
        HiringWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HiringWindow)
        QtCore.QMetaObject.connectSlotsByName(HiringWindow)

    def typefun(self, temp):
        global ttype
        if temp == 1:
            ttype = 1
        elif temp == 2:
            ttype = 2

    def launchDialog(self):
        option = self.options.index(self.comboBox.currentText())
        main.identify(option)
        if option == 0:
            self.getFileName()
        elif option == 1:
            self.getFileNames()
        else:
            print('Got Nothing')

    def launchDialog_2(self):
        option = self.options.index(self.comboBox_2.currentText())

        if option == 0:
            self.getFileName()
        elif option == 1:
            self.getFileNames()
        else:
            print('Got Nothing')

    def getFileName(self):
        file_filter = 'Data File (*.docx *.pdf *.txt);; Text File (*.txt);; PDF File(*.pdf);; Word File(*.docx)'
        response = QFileDialog.getOpenFileName(
            # parent=self,
            caption='Select a data file',
            # directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File (*.docx *.pdf *.txt)'
        )
        self.buttonClicked(response[0])

    def getFileNames(self):
        file_filter = 'Data File (*.docx *.pdf *.txt);; Text File (*.txt);; PDF File(*.pdf);; Word File(*.docx)'
        response = QFileDialog.getOpenFileNames(
            # parent=self,
            caption='Select a data file',
            # directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File (*.docx *.pdf *.txt)'
        )
        self.buttonClicked_2(response[0])

    def retranslateUi(self, HiringWindow):
        _translate = QtCore.QCoreApplication.translate
        HiringWindow.setWindowTitle(_translate("HiringWindow", "HiringWindow"))
        self.label.setText(_translate("HiringWindow", "Select Resume"))
        self.label_2.setText(_translate("HiringWindow", "Select Job Description"))
        self.pushButton.setText(_translate("HiringWindow", "Launch"))
        self.pushButton_2.setText(_translate("HiringWindow", "Launch"))
        self.label_3.setText(_translate("HiringWindow", ""))
        self.pushButton_3.setText(_translate("HiringWindow", "Calculate"))
        self.pushButton_4.setText(_translate("HiringWindow", "Back"))
        self.pushButton_5.setText(_translate("HiringWindow", "More Information"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    HiringWindow = QtWidgets.QMainWindow()
    ui = Ui_HiringWindow()
    ui.setupUi(HiringWindow)
    HiringWindow.show()
    sys.exit(app.exec_())
