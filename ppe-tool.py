# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import configparser
from multiprocessing.sharedctypes import Value
from PyQt5 import QtCore, QtGui, QtWidgets
from confirm import Ui_Dialog


class Ui_PPE_Tool(object):
    def setupUi(self, PPE_Tool):
        self.conf_read = configparser.ConfigParser()
        self.conf_read.read('config.ini')  # reader config.ini
        PPE_Tool.setObjectName("PPE_Tool")
        PPE_Tool.resize(493, 346)
        self.pushButton = QtWidgets.QPushButton(PPE_Tool)
        self.pushButton.setGeometry(QtCore.QRect(270, 290, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        # checked function connection
        self.pushButton.clicked.connect(self.checked)
        self.checkBox = QtWidgets.QCheckBox(PPE_Tool)
        self.checkBox.setChecked(
            bool(self.conf_read['ppe']['belt']))  # defult check value
        self.checkBox.setGeometry(QtCore.QRect(50, 190, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(PPE_Tool)
        self.checkBox_2.setGeometry(QtCore.QRect(50, 100, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(
            bool(self.conf_read['ppe']['helmet']))  # defult check value
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(PPE_Tool)
        self.checkBox_3.setGeometry(QtCore.QRect(50, 160, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setChecked(
            bool(self.conf_read['ppe']['shoe']))  # defult check value
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(PPE_Tool)
        self.checkBox_4.setGeometry(QtCore.QRect(50, 220, 171, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setChecked(
            bool(self.conf_read['ppe']['jacket']))  # defult check value
        self.checkBox_8 = QtWidgets.QCheckBox(PPE_Tool)
        self.checkBox_8.setGeometry(QtCore.QRect(50, 130, 92, 23))
        self.checkBox_8.setChecked(
            bool(self.conf_read['ppe']['mask']))  # defult check value
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.label = QtWidgets.QLabel(PPE_Tool)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 61))
        self.label.setStyleSheet("color: red;\n"
                                 "font-size: 70px;\n"
                                 "font-weight: bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PPE_Tool)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 211, 17))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(PPE_Tool)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 160, 231, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setStyleSheet("border-radius: 10px;")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(1, 99)
        self.value = int(self.conf_read['threshold']['threshold'])
        self.horizontalSlider.setValue(self.value)
        self.horizontalSlider.valueChanged.connect(
            self.slide_it)  # slide_it function connection
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.label_3 = QtWidgets.QLabel(PPE_Tool)
        self.label_3.setGeometry(QtCore.QRect(320, 190, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(PPE_Tool)
        self.label_4.setGeometry(QtCore.QRect(350, 100, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(PPE_Tool)
        QtCore.QMetaObject.connectSlotsByName(PPE_Tool)

    def retranslateUi(self, PPE_Tool):
        _translate = QtCore.QCoreApplication.translate
        PPE_Tool.setWindowTitle(_translate("PPE_Tool", "Dialog"))
        self.pushButton.setText(_translate("PPE_Tool", "save and reboot"))
        self.checkBox.setText(_translate("PPE_Tool", "Safety Belt"))
        self.checkBox_2.setText(_translate("PPE_Tool", "Helmet"))
        self.checkBox_3.setText(_translate("PPE_Tool", "Shoes"))
        self.checkBox_4.setText(_translate("PPE_Tool", "Reflector Jacket"))
        self.checkBox_8.setText(_translate("PPE_Tool", "Mask"))
        self.label.setText(_translate("PPE_Tool", "Hixaa"))
        self.label_2.setText(_translate(
            "PPE_Tool", "EXCELLENCE IN AUTOMATION"))
        self.label_3.setText(_translate("PPE_Tool", "Detector Score"))
        self.label_4.setText(_translate(
            "PPE_Tool", str(self.conf_read['threshold']['threshold'])))

    def checked(self):
        conf_writer = configparser.ConfigParser()
        conf_writer['ppe'] = {}
        conf_writer['threshold'] = {}
        if self.checkBox_4.isChecked() == True:
            conf_writer['ppe']['jacket'] = "True"
        else:
            conf_writer['ppe']['jacket'] = ""
        if self.checkBox_2.isChecked() == True:
            conf_writer['ppe']['helmet'] = "True"
        else:
            conf_writer['ppe']['helmet'] = ""
        if self.checkBox_3.isChecked() == True:
            conf_writer['ppe']['shoe'] = "True"
        else:
            conf_writer['ppe']['shoe'] = ""
        if self.checkBox.isChecked() == True:
            conf_writer['ppe']['belt'] = "True"
        else:
            conf_writer['ppe']['belt'] = ""
        if self.checkBox_8.isChecked() == True:
            conf_writer['ppe']['mask'] = "True"
        else:
            conf_writer['ppe']['mask'] = ""

        conf_writer['threshold']['threshold'] = str(self.value)

        with open('config.ini', 'w') as confile:
            conf_writer.write(confile)

        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setup_Ui(self.window)
        self.window.show()

    def slide_it(self, value):
        self.value = value
        self.label_4.setText(str(value))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PPE_Tool = QtWidgets.QDialog()
    ui = Ui_PPE_Tool()
    ui.setupUi(PPE_Tool)
    PPE_Tool.show()
    sys.exit(app.exec_())
