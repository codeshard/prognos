#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
   conditions.py

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

class Locations(object):
    """dealing with malformed XML values"""
    def __init__(self):
        self.locations = {
            'Pinar del Rio': u'Pronóstico Extendido del Tiempo por Ciudades',
            'La Habana': u'LA HABANA',
            'Varadero': u'VARADERO',
            'Cienfuegos': u'CIENFUEGOS',
            'Cayo Coco': u'CAYO COCO',
            'Camaguey': u'CAMAGÜEY',
            'Holguin': u'HOLGUIN',
            'Santiago De Cuba': u'SANTIAGO DE CUBA'}

class WeatherStatus(object):
    def __init__(self):
        self.weather_status = {
        'Lluvias Ocasionales': ':/actions/images/weather-showers-scattered-day.png',
        'Lluvias dispersas': ':/actions/images/weather-showers-scattered-day.png',
        'Lluvias aisladas': ':/actions/images/weather-showers-scattered-day.png',
        'Lluvias en la Tarde': ':/actions/images/weather-showers-scattered-night.png',
        'Chubascos': ':/actions/images/weather-showers-day.png',
        'Parcialmente Nublado': ':/actions/images/weather-few-clouds.png',
        'Nublado': ':/actions/images/weather-many-clouds.png',
        'Soleado': ':/actions/images/weather-clear.png',
        'Tormentas': ':/actions/images/weather-storm-day.png'}

class Temperatures(object):
    def __init__(self):
        self.temperatures = {
        '0': 'Celcius °C',
        '1': 'Fahrenheit °F',
        '2': 'Kelvin K'}
