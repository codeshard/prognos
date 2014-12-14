#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
   util.py

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

class ConvertTemperature(object):
    def __init__(self):
        pass

    def convert_temp(self, t_to, t_input):
        input = float(str(t_input))
        output = 0

        if t_to == "0":
            output = input
        elif t_to == "1":
            output = ((input + 273.15) * 1.8) - 459.67
        elif t_to == "2":
            output = input + 273.15
        return str(output)
