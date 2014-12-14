#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
   prognos_preferences.py

   Copyright 2014 Ozkar L. Garcell <ozkar.garcell@gmail.com>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

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

class OptionsDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(OptionsDialog, self).__init__(parent)
        self.setWindowTitle('Opciones')
        self.resize(400, 300)
        self.verticalLayout_7 = QtGui.QVBoxLayout(self)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.groupBox_2 = QtGui.QGroupBox(self)
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox_location = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_location.addItem("PINAR DEL RIO")
        self.comboBox_location.addItem("LA HABANA")
        self.comboBox_location.addItem("VARADERO")
        self.comboBox_location.addItem("CIENFUEGOS")
        self.comboBox_location.addItem("CAYO COCO")
        self.comboBox_location.addItem(u"CAMAGÜEY")
        self.comboBox_location.addItem("HOLGUIN")
        self.comboBox_location.addItem("SANTIAGO DE CUBA")
        self.horizontalLayout.addWidget(self.comboBox_location)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self)
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.horizontalLayout_2.addWidget(self.label_6)
        self.comboBox_temperature = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_temperature.addItem(_translate(None, "Celcius °C", None))
        self.comboBox_temperature.addItem(_translate(None, "Fahrenheit °F", None))
        self.comboBox_temperature.addItem("Kelvin K")
        self.horizontalLayout_2.addWidget(self.comboBox_temperature)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.horizontalLayout_3.addWidget(self.label_7)
        self.comboBox_language = QtGui.QComboBox(self.groupBox_3)
        self.horizontalLayout_3.addWidget(self.comboBox_language)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self)
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.horizontalLayout_4.addWidget(self.checkBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout = QtGui.QGridLayout()
        self.label = QtGui.QLabel(self.groupBox)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_host = QtGui.QLineEdit(self.groupBox)
        self.gridLayout.addWidget(self.lineEdit_host, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.lineEdit_port = QtGui.QLineEdit(self.groupBox)
        self.gridLayout.addWidget(self.lineEdit_port, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_user = QtGui.QLineEdit(self.groupBox)
        self.gridLayout.addWidget(self.lineEdit_user, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.lineEdit_passwd = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_passwd.setEchoMode(QtGui.QLineEdit.Password)
        self.gridLayout.addWidget(self.lineEdit_passwd, 1, 3, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.buttonBox.accepted.connect(self._settings)
        self.buttonBox.rejected.connect(self.close)

        self.groupBox_2.setTitle(_translate(None, "Ubicación", None))
        self.label_5.setText(_translate(None, "Seleccione Ubicación:", None))
        self.groupBox_3.setTitle(_translate(None, "General:", None))
        self.label_6.setText(_translate(None, "Temperatura:", None))
        self.label_7.setText(_translate(None, "Lenguaje:", None))
        self.groupBox.setTitle(_translate(None, "Autenticación", None))
        self.checkBox.setText(_translate(None, "Usar HTTP-Proxy", None))
        self.label.setText(_translate(None, "Host:", None))
        self.lineEdit_host.setInputMask(_translate(None, "000.000.000.000; ", None))
        self.label_2.setText(_translate(None, "Puerto:", None))
        self.lineEdit_port.setInputMask(_translate(None, "0000; ", None))
        self.label_3.setText(_translate(None, "Usuario:", None))
        self.label_4.setText(_translate(None, "Contraseña:", None))

        self.checkBox.stateChanged.connect(self.auth_tokens)
        self._init()
        self.auth_tokens()

    def _init(self):
        settings = QtCore.QSettings(
            QtCore.QDir.homePath() + '/.prognos/config.ini',
            QtCore.QSettings.IniFormat)
        location = settings.value("location").toString()
        temperature = settings.value("temperature").toString()
        language = settings.value("language").toString()
        proxy = settings.value("proxy").toString()
        host = settings.value("host").toString()
        port = settings.value("port").toString()
        user = settings.value("user").toString()
        passwd = settings.value("passwd").toString()
        self.comboBox_location.setCurrentIndex(self.comboBox_location.findText(location))
        self.comboBox_temperature.setCurrentIndex(self.comboBox_temperature.findText(temperature))
        self.comboBox_language.setCurrentIndex(self.comboBox_language.findText(language))
        if proxy == 'true':
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)
        self.lineEdit_host.setText(host)
        self.lineEdit_port.setText(port)
        self.lineEdit_user.setText(user)
        self.lineEdit_passwd.setText(passwd)

    def _settings(self):
        settings = QtCore.QSettings(
            QtCore.QDir.homePath() + '/.prognos/config.ini',
            QtCore.QSettings.IniFormat)
        settings.setValue("location", self.comboBox_location.currentText())
        settings.setValue("temperature", self.comboBox_temperature.currentText())
        settings.setValue("language", self.comboBox_language.currentText())
        settings.setValue("proxy", self.checkBox.isChecked())
        settings.setValue("host", self.lineEdit_host.text())
        settings.setValue("port", self.lineEdit_port.text())
        settings.setValue("user", self.lineEdit_user.text())
        settings.setValue("passwd", self.lineEdit_passwd.text())
        self.close()

    def auth_tokens(self):
        if self.checkBox.isChecked():
            self.lineEdit_host.setEnabled(True)
            self.lineEdit_port.setEnabled(True)
            self.lineEdit_user.setEnabled(True)
            self.lineEdit_passwd.setEnabled(True)
        else:
            self.lineEdit_host.setEnabled(False)
            self.lineEdit_port.setEnabled(False)
            self.lineEdit_user.setEnabled(False)
            self.lineEdit_passwd.setEnabled(False)
