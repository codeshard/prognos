#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
   prognos_extended.py

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

class ExtendedDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ExtendedDialog, self).__init__(parent)
        self.setWindowTitle('Pronostico Extendido')
        self.resize(558, 338)
        self.verticalLayout_2 = QtGui.QVBoxLayout(self)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.label = QtGui.QLabel(self)
        self.label.setStyleSheet(
            "font-size:18pt;")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setText(_translate(None, "Pronóstico Extendido", None))
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtGui.QTableWidget(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        QtCore.QMetaObject.connectSlotsByName(self)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate(None, "Día", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate(None, "T Máxima", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate(None, "T Mínima", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate(None, "Pronóstico", None))
