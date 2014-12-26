#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
   weather.py

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

import re
import time
import urllib2
from lxml import etree

from database import PrognosDB
from conditions import Locations


class CubanWeather(object):
    def __init__(self):
        self.weather_data = {}
        self.location = Locations()
        self.db = PrognosDB()
        self.db.create_connection()
        self.db.create_table()
        self.year = time.strftime("%Y")
        self.month = time.strftime("%m")
        self.day = time.strftime("%d")

    def proxy_authenticate(self, host, port, user, passwd):
        cmd = ''.join([
            'http://',
            '{u}'.format(u=user),
            ':',
            '{p}'.format(p=passwd),
            '@',
            '{0}:{1}'.format(host, port)])
        proxy = urllib2.ProxyHandler({'http': cmd})
        auth = urllib2.HTTPBasicAuthHandler()
        opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
        urllib2.install_opener(opener)

    def fetch_weather(self, location):
        title = u''
        values = []
        conn = urllib2.urlopen(u'http://www.met.inf.cu/asp/genesis.asp?TB0=RSSFEED')
        t_data = conn.read()
        conn.close()
        t_root = etree.fromstring(t_data)
        item = t_root.findall('channel/title')
        for item in t_root.xpath('/rss/channel/item'):
            if item.xpath(u"./title/text()")[0] == location:
                title = item.xpath(u"./title/text()")[0]
                description = item.xpath("./description/text()")[0]
                dataCrop = re.findall(r'<td>\W*?.*?</td>', description)
                for data in dataCrop:
                    values.append(re.sub("<.*?>", "", data))
        title = next((k for k, v in self.location.locations.items() if v == title), None)
        self.weather_data['location'] = title
        self.weather_data['current_month_day'] = values[0]
        self.weather_data['current_day_temp'] = values[1]
        self.weather_data['current_night_temp'] = values[2]
        self.weather_data['current_day_weather'] = values[3]
        store_data = [
            (int(self.year), int(self.month), int(values[0]), title.encode('utf-8'), int(values[1]), int(values[2]), str(values[3])),
            (int(self.year), int(self.month), int(values[4]), title.encode('utf-8'), int(values[5]), int(values[6]), str(values[7])),
            (int(self.year), int(self.month), int(values[8]), title.encode('utf-8'), int(values[9]), int(values[10]), str(values[11])),
            (int(self.year), int(self.month), int(values[12]), title.encode('utf-8'), int(values[13]), int(values[14]), str(values[15])),
            (int(self.year), int(self.month), int(values[16]), title.encode('utf-8'), int(values[17]), int(values[18]), str(values[19])),
            ]
        self.db.insert_query(store_data)
        return self.weather_data
