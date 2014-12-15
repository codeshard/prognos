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
from prognos_extended import ExtendedDialog
from conditions import Locations, WeatherStatus
from weather import CubanWeather
from database import PrognosDB
from util import ConvertTemperature

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

        #time vars
        self.day_hour  = time.strftime("%H")
        self.week_day = time.strftime("%A")
        self.month = time.strftime("%b")
        self.month_int = time.strftime("%m")
        self.day = time.strftime("%d")

        self.create_actions()
        self.create_toolbar()

        self.label_weather_image.filename = ''
        self.read_settings()
        self.get_current_date()

        self.create_trayIcon()
        self.trayIcon.show()

        self.cw = CubanWeather()
        self.location = Locations()
        self.status = WeatherStatus()
        self.db = PrognosDB()
        self.db.create_connection()
        self.ct = ConvertTemperature()

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

    def create_trayIcon(self):
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
        if self.day_hour > '01' and self.day_hour < '18':
            self.show_trayIcon_message(
                self.settings.value("location").toString(),
                self.settings.value("Weather/weather_pixmap").toString(),
                self.settings.value("Weather/current_day_temp").toString(),
                self.settings.value("Weather/current_day_weather").toString())
        else:
            self.show_trayIcon_message(
                self.settings.value("location").toString(),
                self.settings.value("Weather/weather_pixmap").toString(),
                self.settings.value("Weather/current_night_temp").toString(),
                self.settings.value("Weather/current_day_weather").toString())

    def show_trayIcon_message(self, location, pixmap, temp, weather):
        tooltip_message = ('{l}, Cuba'
            u'<img src="{p}" width="48" height="48"/><br>'
            u'Temperatura: <span style="font-weight:600;">{t}°C</span><br>'
            u'Pronóstico: <span style="font-weight:600;">{w}</span>').format(l=location, p=pixmap, t=temp, w=weather)
        self.trayIcon.setToolTip(tooltip_message)

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
            self,
            triggered=self.extended)
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
        self.settings = QtCore.QSettings(
            QtCore.QDir.homePath() + '/.prognos/config.ini',
            QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("UTF-8")
        pos = self.settings.value(
            "pos",
            QtCore.QPoint(526, 238),
            type=QtCore.QPoint)
        size = self.settings.value(
            "size",
            QtCore.QSize(270, 379),
            type=QtCore.QSize)
        self.resize(size)
        self.move(pos)

    def write_settings(self):
        self.settings = QtCore.QSettings(
            QtCore.QDir.homePath() + '/.prognos/config.ini',
            QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("UTF-8")
        self.settings.setValue("pos", self.pos())
        self.settings.setValue("size", self.size())

    def closeEvent(self, event):
        self.write_settings()
        self.save_data()
        event.accept()

    def get_current_date(self):
        self.label_date.setText(str(self.week_day) + ", " + str(self.month) + " " + str(self.day))

    def update_ui(self, weather):
        icon = QtGui.QIcon()
        if str(weather) == 'Lluvias Ocasionales':
            icon.addPixmap(QtGui.QPixmap(self.status.weather_status[weather]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(self.status.weather_status[weather]))
            self.label_weather_image.filename = self.status.weather_status[weather]

        if str(weather) == 'Lluvias dispersas':
            icon.addPixmap(QtGui.QPixmap(self.status.weather_status[weather]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(self.status.weather_status[weather]))
            self.label_weather_image.filename = self.status.weather_status[weather]

        if str(weather) == 'Lluvias aisladas':
            icon.addPixmap(QtGui.QPixmap(self.status.weather_status[weather]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(self.status.weather_status[weather]))
            self.label_weather_image.filename = self.status.weather_status[weather]

        if str(weather) == 'Lluvias en la Tarde':
            icon.addPixmap(QtGui.QPixmap(self.status.weather_status[weather]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(self.status.weather_status[weather]))
            self.label_weather_image.filename = self.status.weather_status[weather]

        if str(weather) == 'Chubascos':
            icon.addPixmap(QtGui.QPixmap(self.status.weather_status[weather]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(self.status.weather_status[weather]))
            self.label_weather_image.filename = self.status.weather_status[weather]

        if str(weather) == 'Parcialmente Nublado':
            icon.addPixmap(QtGui.QPixmap(self.status.weather_status[weather]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(self.status.weather_status[weather]))
            self.label_weather_image.filename = self.status.weather_status[weather]

        if str(weather) == 'Nublado':
            icon.addPixmap(QtGui.QPixmap(self.status.weather_status[weather]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(self.status.weather_status[weather]))
            self.label_weather_image.filename = self.status.weather_status[weather]

        if str(weather) == 'Soleado':
            icon.addPixmap(QtGui.QPixmap(self.status.weather_status[weather]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(self.status.weather_status[weather]))
            self.label_weather_image.filename = self.status.weather_status[weather]

        if str(weather) == 'Tormentas':
            icon.addPixmap(QtGui.QPixmap(self.status.weather_status[weather]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.label_weather_image.setPixmap(QtGui.QPixmap(self.status.weather_status[weather]))
            self.label_weather_image.filename = self.status.weather_status[weather]

    def calculate_temperature(self, temp):
        if self.settings.value("temperature").toString() == '0':
            return u' '.join([self.ct.convert_temp('0', temp), u'°C'])
        elif self.settings.value("temperature").toString() == '1':
            return u' '.join([self.ct.convert_temp('1', temp), u'°F'])
        elif self.settings.value("temperature").toString() == '2':
            return u' '.join([self.ct.convert_temp('2', temp), 'K'])

    def gather_data(self):
        prov = self.settings.value("location").toString().toUtf8()
        data = self.db.select_query(self.month_int, self.day, prov)
        if data:
            for row in data:
                self.day_temp = row[5]
                self.night_temp = row[6]
                self.weather = row[7]
                if self.day_hour > '01' and self.day_hour < '18':
                    self.label_temperature.setText(self.calculate_temperature(self.day_temp))
                else:
                    self.label_temperature.setText(self.calculate_temperature(self.night_temp))
                self.label_weather_status.setText(_translate(None, str(self.weather), None))
                self.update_ui(self.weather)
        else:
            proxy = self.settings.value("proxy").toString()
            host = self.settings.value("host").toString()
            port = self.settings.value("port").toString()
            user = self.settings.value("user").toString()
            passwd = self.settings.value("passwd").toString()
            if not self.cw.proxy_authenticate(host, port, user, passwd):
                self.cw.fetch_weather(u'' + prov)
                self.day_temp = self.cw.weather_data['current_day_temp']
                self.night_temp = self.cw.weather_data['current_night_temp']
                self.weather = self.cw.weather_data['current_day_weather']
                if self.day_hour > '01' and self.day_hour < '18':
                    self.label_temperature.setText(self.calculate_temperature(self.day_temp))
                else:
                    self.label_temperature.setText(self.calculate_temperature(self.night_temp))
                self.label_weather_status.setText(_translate(None, str(self.weather), None))
                self.update_ui(self.weather)
            else:
                QtGui.QMessageBox.critical(None, "Prognos",
                u"Red no disponible o parametros de conexión mal configurados.")

        self.setWindowTitle(_translate(None, prov, None))

    def load_data(self):
        if self.settings.contains('Weather/current_day_temp'):
            day_hour  = time.strftime("%H")
            if day_hour > '01' and day_hour < '18':
                self.label_temperature.setText(self.calculate_temperature(self.settings.value("Weather/current_day_temp").toString()))
            else:
                self.label_temperature.setText(self.calculate_temperature(self.settings.value("Weather/current_night_temp").toString()))
            self.label_weather_image.setPixmap(QtGui.QPixmap(str(self.settings.value("Weather/weather_pixmap").toString())))
            self.label_weather_status.setText(str(self.settings.value("Weather/current_day_weather").toString()))
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(QtGui.QPixmap(str(self.settings.value("Weather/weather_pixmap").toString()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            self.trayIcon.setIcon(icon)
            self.setWindowTitle(self.settings.value("location").toString())
        else:
            QtGui.QMessageBox.warning(None, "Prognos",
                "Al parecer <b>Prognos</b> no se ha configurado para su uso "
                "por favor, configure el programa...")
            opt = OptionsDialog(self)
            opt.show()

    def save_data(self):
        if self.cw.weather_data:
            self.settings.setIniCodec("UTF-8")
            self.settings.beginGroup("Weather")
            self.settings.setValue("current_month_day", str(self.cw.weather_data['current_month_day']))
            self.settings.setValue("current_day_temp", int(self.cw.weather_data['current_day_temp']))
            self.settings.setValue("current_night_temp", int(self.cw.weather_data['current_night_temp']))
            self.settings.setValue("current_day_weather", str(self.cw.weather_data['current_day_weather']))
            self.settings.setValue("weather_pixmap", str(self.label_weather_image.filename))
            self.settings.endGroup()

    def options(self):
        opt = OptionsDialog(self)
        opt.show()

    def extended(self):
        prov = self.settings.value("location").toString().toUtf8()
        ext = ExtendedDialog(self)
        ext.load_data(prov)
        ext.show()

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
