# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prognos_v2.ui'
#
# Created: Wed Dec  3 10:32:25 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(270, 379)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/weather-clear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_date = QtGui.QLabel(self.centralwidget)
        self.label_date.setObjectName(_fromUtf8("label_date"))
        self.verticalLayout.addWidget(self.label_date)
        self.label_weather_image = QtGui.QLabel(self.centralwidget)
        self.label_weather_image.setMinimumSize(QtCore.QSize(256, 256))
        self.label_weather_image.setMaximumSize(QtCore.QSize(256, 256))
        self.label_weather_image.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_weather_image.setText(_fromUtf8(""))
        self.label_weather_image.setPixmap(QtGui.QPixmap(_fromUtf8(":/actions/images/weather-clouds.png")))
        self.label_weather_image.setScaledContents(True)
        self.label_weather_image.setObjectName(_fromUtf8("label_weather_image"))
        self.verticalLayout.addWidget(self.label_weather_image)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setFrameShape(QtGui.QFrame.HLine)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_temperature = QtGui.QLabel(self.centralwidget)
        self.label_temperature.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_temperature.setObjectName(_fromUtf8("label_temperature"))
        self.horizontalLayout.addWidget(self.label_temperature)
        self.label_weather_status = QtGui.QLabel(self.centralwidget)
        self.label_weather_status.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_weather_status.setObjectName(_fromUtf8("label_weather_status"))
        self.horizontalLayout.addWidget(self.label_weather_status)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Prognos", None))
        self.label_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">MIERCOLES, DIC 03</span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "TextLabel", None))
        self.label_temperature.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">28 °C</span></p></body></html>", None))
        self.label_weather_status.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Parcialmente Nublado</span></p></body></html>", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

import prognos_rc
