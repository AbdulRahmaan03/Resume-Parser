from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

import main

master_dict = {}


class Ui_MoreInformation(object):
    def openHiringWindow(self):
        from HiringWindow import Ui_HiringWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HiringWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def loaddata(self):
        global master_dict
        table_value = main.show()
        try:
            master_dict = {}
            for i, j in enumerate(table_value[0]):
                master_dict[i] = {}
                master_dict[i]["Name"] = j
            for i, j in enumerate(table_value[1]):
                master_dict[i]["Skill"] = j
            for i, j in enumerate(table_value[2]):
                master_dict[i + 1]["Similarity"] = j
            for i, j in enumerate(table_value[3]):
                master_dict[i + 1]["Value"] = j
            for i, j in enumerate(table_value[4]):
                master_dict[i]["Location"] = j

            self.tableWidget.setRowCount(len(master_dict))
            row = 0
            for i in master_dict:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(master_dict[i]["Name"]))
                if master_dict[i].get('Skill'):
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(' '.join(master_dict[i]["Skill"])))
                    self.tableWidget.setStyleSheet("*{\n"
                                                   "    font: 10pt \"Arial Rounded MT Bold\";\n"
                                                   "    color:\"cyan\";\n"
                                                   "    background-color:rgba(0,0,0,0);\n"
                                                   "}\n")
                    # item.setForeground(QBrush(QColor(0, 255, 0)))
                else:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(' '))
                if master_dict[i].get('Similarity'):
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(' '.join(master_dict[i]["Similarity"])))
                else:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(' '))
                if master_dict[i].get('Value'):
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(master_dict[i]["Value"])))
                else:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(' '))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(master_dict[i]["Location"]))
                row = row + 1
        except Exception:
            print("its ok")

    def open_file(self, row, column):
        if column == 4:
            webbrowser.open(master_dict[row]["Location"])

    def finish(self):
        exit()

    def setupUi(self, MoreInformation):
        MoreInformation.setObjectName("MoreInformation")
        MoreInformation.resize(1420, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MoreInformation.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MoreInformation)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1420, 800))
        self.widget.setStyleSheet(
            "QWidget#widget{background-image:url(C:/Users/user/PycharmProjects/pythonProject/mainbg)}\n"
            "")
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.tableWidget.setGeometry(QtCore.QRect(190, 70, 1021, 621))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnWidth(0, 100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.setColumnWidth(1, 300)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(2, 350)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3, 150)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.setColumnWidth(4, 119)
        self.tableWidget.cellDoubleClicked.connect(self.open_file)
        self.loaddata()
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(50, 710, 110, 50))
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
        self.pushButton.clicked.connect(lambda: [self.openHiringWindow(), MoreInformation.hide()])
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(1250, 710, 110, 50))
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
        self.pushButton_2.clicked.connect(lambda: self.finish())
        self.pushButton_2.setObjectName("pushButton")
        MoreInformation.setCentralWidget(self.centralwidget)

        self.retranslateUi(MoreInformation)
        QtCore.QMetaObject.connectSlotsByName(MoreInformation)

    def retranslateUi(self, MoreInformation):
        _translate = QtCore.QCoreApplication.translate
        MoreInformation.setWindowTitle(_translate("MoreInformation", "MoreInformation"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MoreInformation", "File Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MoreInformation", "Skills"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MoreInformation", "Word Count"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MoreInformation", "Similarity Score"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MoreInformation", "Link"))
        self.pushButton.setText(_translate("HiringWindow", "Back"))
        self.pushButton_2.setText(_translate("HiringWindow", "Finish"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MoreInformation = QtWidgets.QMainWindow()
    ui = Ui_MoreInformation()
    ui.setupUi(MoreInformation)
    MoreInformation.show()
    sys.exit(app.exec_())
