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
import urllib2
from lxml import etree


class CubanWeather(object):
    def __init__(self):
        self.weather_data = {}

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
        title = ''
        description = ''
        values = []
        conn = urllib2.urlopen(u'http://www.met.inf.cu/asp/genesis.asp?TB0=RSSFEED')
        t_data = conn.read()
        conn.close()
        t_root = etree.fromstring(t_data)
        item = t_root.findall('channel/title')
        for item in t_root.xpath('/rss/channel/item'):
            if item.xpath("./title/text()")[0] == location:
                title = item.xpath("./title/text()")[0]
                description = item.xpath("./description/text()")[0]
                dataCrop = re.findall(r'<td>\W*?.*?</td>', description)
                for data in dataCrop:
                    values.append(re.sub("<.*?>", "", data))
        self.weather_data['location'] = title
        self.weather_data['current_month_day'] = values[0]
        self.weather_data['current_day_temp'] = values[1]
        self.weather_data['current_night_temp'] = values[2]
        self.weather_data['current_day_weather'] = values[3]
        return self.weather_data
