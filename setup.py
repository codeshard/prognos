#!/usr/bin/env python

from distutils.core import setup

setup(
    name='prognos',
    version='0.1',
    description='Weather Status Monitoring Application for Cuba',
    author='Ozkar L. Garcell',
    author_email='ozkar@elechol,une.cu',
    url='https://github.com/codeshard/prognos',
    license='Apache License, Version 2.0',
    packages=['prognos'],
    data_files=[('/usr/share/applications',['share/prognos.desktop']),
            ('/usr/share/icons',['prognos/images/prognos.png']),
            ('/usr/share/prognos/images',[
                'prognos/images/weather-clear-night.png',
                'prognos/images/weather-clear.png',
                'prognos/images/weather-clouds-night.png',
                'prognos/images/weather-clouds.png',
                'prognos/images/weather-few-clouds-night.png',
                'prognos/images/weather-few-clouds.png',
                'prognos/images/weather-many-clouds.png',
                'prognos/images/weather-mist.png',
                'prognos/images/weather-none-available.png',
                'prognos/images/weather-showers-day.png',
                'prognos/images/weather-showers-night.png',
                'prognos/images/weather-showers-scattered-day.png',
                'prognos/images/weather-showers-scattered-night.png',
                'prognos/images/weather-showers-scattered.png',
                'prognos/images/weather-storm-day.png',
                'prognos/images/weather-storm-night.png']),
            ('/usr/share/doc/prognos', ['README.md','LICENSE','CHANGELOG'])],
        scripts = ["bin/prognos"]
        )
