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
            'Santiago de Cuba': u'SANTIAGO DE CUBA'}
