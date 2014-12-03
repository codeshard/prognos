#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
   prognos.py

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

import sys
import time

from PyQt4 import QtCore, QtGui

import prognos_qrc
from prognos_preferences import OptionsDialog
from conditions import Locations
from weather import CubanWeather

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

class Prognos(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Prognos, self).__init__(parent)
        self.resize(270, 379)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget = QtGui.QWidget(self)
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.label_date = QtGui.QLabel(self.centralwidget)
        self.label_date.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_date.setStyleSheet(
            "font-size:18pt;"
            "font-weight:600;")
        self.verticalLayout.addWidget(self.label_date)
        self.label_weather_image = QtGui.QLabel(self.centralwidget)
        self.label_weather_image.setMinimumSize(QtCore.QSize(256, 256))
        self.label_weather_image.setMaximumSize(QtCore.QSize(256, 256))
        self.label_weather_image.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_weather_image.setScaledContents(True)
        self.verticalLayout.addWidget(self.label_weather_image)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setFrameShape(QtGui.QFrame.HLine)
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.label_temperature = QtGui.QLabel(self.centralwidget)
        self.label_temperature.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_temperature.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_temperature.setStyleSheet(
            "font-size:18pt;")
        self.horizontalLayout.addWidget(self.label_temperature)
        self.label_weather_status = QtGui.QLabel(self.centralwidget)
        self.label_weather_status.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_weather_status.setAlignment(QtCore.Qt.AlignHCenter)
        self.label_weather_status.setStyleSheet(
            "font-size:12pt;")
        self.horizontalLayout.addWidget(self.label_weather_status)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Prognos")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/images/weather-none-available.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.create_actions()
        self.create_toolbar()
        self.create_tray_icon()
        self.trayIcon.setIcon(QtGui.QIcon('":/actions/images/weather-none-available.png"'))
        self.trayIcon.show()

        self.label_weather_image.filename = ''
        self.read_settings()
        self.get_current_date()

        self.cw = CubanWeather()
        self.location = Locations()

        self.load_data()

    def create_toolbar(self):
        self.toolBar = QtGui.QToolBar(self)
        self.toolBar.addAction(self.refresh_action)
        self.toolBar.addAction(self.extended_action)
        self.toolBar.addAction(self.options_action)
        self.toolBar.addAction(self.about_action)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.quit_action)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

    def create_tray_icon(self):
         self.trayIconMenu = QtGui.QMenu(self)
         self.trayIconMenu.addAction(self.minimize_action)
         self.trayIconMenu.addAction(self.restore_action)
         self.trayIconMenu.addAction(self.refresh_action)
         self.trayIconMenu.addAction(self.extended_action)
         self.trayIconMenu.addAction(self.options_action)
         self.trayIconMenu.addAction(self.about_action)
         self.trayIconMenu.addSeparator()
         self.trayIconMenu.addAction(self.quit_action)
         self.trayIcon = QtGui.QSystemTrayIcon(self)
         self.trayIcon.setContextMenu(self.trayIconMenu)

    def create_actions(self):
        self.minimize_action = QtGui.QAction(
            self.style().standardIcon(QtGui.QStyle.SP_TitleBarMinButton),
            self.tr(u'Minimizar'),
            self,
            triggered=self.hide)
        self.restore_action = QtGui.QAction(
            self.style().standardIcon(QtGui.QStyle.SP_TitleBarNormalButton),
            self.tr(u'Restaurar'),
            self,
            triggered=self.showNormal)
        self.refresh_action = QtGui.QAction(
            self.style().standardIcon(QtGui.QStyle.SP_BrowserReload),
            self.tr(u'Actualizar'),
            self,
            triggered=self.gather_data)
        self.extended_action = QtGui.QAction(
            self.style().standardIcon(QtGui.QStyle.SP_ComputerIcon),
            self.tr(u'Pronóstico'),
            self)
        self.options_action = QtGui.QAction(
            self.style().standardIcon(QtGui.QStyle.SP_FileDialogDetailedView),
            self.tr(u'Opciones'),
            self,
            triggered=self.options)
        self.about_action = QtGui.QAction(
            self.style().standardIcon(QtGui.QStyle.SP_MessageBoxInformation),
            self.tr(u'Acerca de...'),
            self,
            triggered=self.about)
        self.quit_action = QtGui.QAction(
            self.style().standardIcon(QtGui.QStyle.SP_DialogCloseButton),
            self.tr(u'Salir'),
            self,
            triggered=self.close)

    def read_settings(self):
        settings = QtCore.QSettings(
            QtCore.QDir.homePath() + '/.prognos/config.ini',
            QtCore.QSettings.IniFormat)
        pos = settings.value(
            "pos",
            QtCore.QPoint(526, 238),
            type=QtCore.QPoint)
        size = settings.value(
            "size",
            QtCore.QSize(270, 379),
            type=QtCore.QSize)
        self.resize(size)
        self.move(pos)

    def write_settings(self):
        settings = QtCore.QSettings(
            QtCore.QDir.homePath() + '/.prognos/config.ini',
            QtCore.QSettings.IniFormat)
        settings.setValue("pos", self.pos())
        settings.setValue("size", self.size())

    def closeEvent(self, event):
        self.write_settings()
        self.save_data()
        event.accept()

    def get_current_date(self):
        week_day = time.strftime("%A")
        month = time.strftime("%b")
        day = time.strftime("%d")
        self.label_date.setText(str(week_day) + ", " + str(month) + " " + str(day))

    def gather_data(self):
        settings = QtCore.QSettings(
            QtCore.QDir.homePath() + '/.prognos/config.ini',
            QtCore.QSettings.IniFormat)
        prov = settings.value("location").toString()
        temperature = settings.value("temperature").toString()
        language = settings.value("language").toString()
        proxy = settings.value("proxy").toString()
        host = settings.value("host").toString()
        port = settings.value("port").toString()
        user = settings.value("user").toString()
        passwd = settings.value("passwd").toString()
        self.cw.proxy_authenticate(host, port, user, passwd)
        self.cw.fetch_weather(self.location.locations[str(prov)])
        day_hour  = time.strftime("%H")
        if day_hour > '01' and day_hour < '18':
            self.label_temperature.setText(_translate(None, str(self.cw.weather_data['current_day_temp']) + "°C", None))
        else:
            self.label_temperature.setText(_translate(None, str(self.cw.weather_data['current_night_temp']) + "°C", None))
        self.label_weather_status.setText(_translate(None, str(self.cw.weather_data['current_day_weather']), None))
        self.setWindowTitle(str(prov))
        icon = QtGui.QIcon()
        if str(self.cw.weather_data['current_day_weather']) == 'Lluvias Ocasionales':
            icon.addPixmap(QtGui.QPixmap(":/actions/images/weather-showers-scattered-day.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(":/actions/images/weather-showers-scattered-day.png"))
            self.label_weather_image.filename = ":/actions/images/weather-showers-scattered-day.png"

        if str(self.cw.weather_data['current_day_weather']) == 'Lluvias aisladas':
            icon.addPixmap(QtGui.QPixmap(":/actions/images/weather-showers-scattered-day.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(":/actions/images/weather-showers-scattered-day.png"))
            self.label_weather_image.filename = ":/actions/images/weather-showers-scattered-day.png"

        if str(self.cw.weather_data['current_day_weather']) == 'Lluvias en la Tarde':
            icon.addPixmap(QtGui.QPixmap(":/actions/images/weather-showers-scattered-night.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(":/actions/images/weather-showers-scattered-night.png"))
            self.label_weather_image.filename = ":/actions/images/weather-showers-scattered-night.png"

        if str(self.cw.weather_data['current_day_weather']) == 'Chubascos':
            icon.addPixmap(QtGui.QPixmap(":/actions/images/weather-showers-day.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(":/actions/images/weather-showers-day.png"))
            self.label_weather_image.filename = ":/actions/images/weather-showers-day.png"

        if str(self.cw.weather_data['current_day_weather']) == 'Parcialmente Nublado':
            icon.addPixmap(QtGui.QPixmap(":/actions/images/weather-few-clouds.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(":/actions/images/weather-few-clouds.png"))
            self.label_weather_image.filename = ":/actions/images/weather-few-clouds.png"

        if str(self.cw.weather_data['current_day_weather']) == 'Nublado':
            icon.addPixmap(QtGui.QPixmap(":/actions/images/weather-many-clouds.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(":/actions/images/weather-many-clouds.png"))
            self.label_weather_image.filename = ":/actions/images/weather-many-clouds.png"

        if str(self.cw.weather_data['current_day_weather']) == 'Soleado':
            icon.addPixmap(QtGui.QPixmap(":/actions/images/weather-clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(":/actions/images/weather-clear.png"))
            self.label_weather_image.filename = ":/actions/images/weather-clear.png"

        settings.beginGroup("Weather")
        settings.setValue("current_day_temp", int(self.cw.weather_data['current_day_temp']))
        settings.setValue("current_night_temp", int(self.cw.weather_data['current_night_temp']))
        settings.setValue("current_day_weather", str(self.cw.weather_data['current_day_weather']))
        settings.setValue("weather_pixmap", str(self.label_weather_image.filename))
        settings.endGroup()

    def load_data(self):
        settings = QtCore.QSettings(
            QtCore.QDir.homePath() + '/.prognos/config.ini',
            QtCore.QSettings.IniFormat)
        if settings.contains('Weather/current_day_temp'):
            day_hour  = time.strftime("%H")
            if day_hour > '01' and day_hour < '18':
                self.label_temperature.setText(_translate(None, settings.value("Weather/current_day_temp").toString() + "°C", None))
            else:
                self.label_temperature.setText(_translate(None, settings.value("Weather/current_night_temp").toString() + "°C", None))
            self.label_weather_image.setPixmap(QtGui.QPixmap(str(settings.value("Weather/weather_pixmap").toString())))
            self.label_weather_status.setText(str(settings.value("Weather/current_day_weather").toString()))
            self.setWindowTitle(str(settings.value("location").toString()))
        else:
            QtGui.QMessageBox.warning(None, "Prognos",
                "Al parecer <b>Prognos</b> no se ha configurado para su uso "
                "por favor, configure el programa...")
            opt = OptionsDialog(self)
            opt.show()

    def save_data(self):
        settings = QtCore.QSettings(
            QtCore.QDir.homePath() + '/.prognos/config.ini',
            QtCore.QSettings.IniFormat)
        if self.cw.weather_data:
            settings.beginGroup("Weather")
            settings.setValue("current_day_temp", int(self.cw.weather_data['current_day_temp']))
            settings.setValue("current_night_temp", int(self.cw.weather_data['current_night_temp']))
            settings.setValue("current_day_weather", str(self.cw.weather_data['current_day_weather']))
            settings.setValue("weather_pixmap", str(self.label_weather_image.filename))
            settings.endGroup()

    def options(self):
        opt = OptionsDialog(self)
        opt.show()

    def about(self):
        QtGui.QMessageBox.about(
            self,
            'Prognos',
            self.tr("""<p>Author: <b>Ozkar L. Garcell</b> <a href="mailto:ozkar@elechol.une.cu">ozkar@elechol.une.cu</a>
                        <p>Aplicacion simple para monitorear el estado del tiempo en CUBA.
                        <p>Website: <a href="https://github.com/codeshard/prognos-qt"> https://github.com/codeshard/prognos</a>
                        <p>Origenes de Datos: <a href="http://www.met.inf.cu/asp/genesis.asp?TB0=RSSFEED"> http://www.met.inf.cu/</a>."""))

def main():
    app = QtGui.QApplication(sys.argv)
    if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        QtGui.QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        sys.exit(1)
    prognos = Prognos()
    prognos.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        QtGui.QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        sys.exit(1)
    prognos = Prognos()
    prognos.show()
    sys.exit(app.exec_())
