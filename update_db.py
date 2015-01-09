#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import time
import sys
import os
try:
    from bs4 import BeautifulSoup as bs
    import requests
    import argparse
except ImportError:
    print('Please install requests/bs4/argparse modules')
    sys.exit(1)


def get_city_id(id):
    city_list, id_list = [], []
    city_id = str(id)
    id_patern = re.compile('meeting\.html\?p1=(\d{1,4})')
    url = 'http://www.timeanddate.com/worldclock/city.html?n=' + city_id
    city = requests.get(url).url.split('/')[-1]
    time.sleep(0.5)
    return city + '=' + city_id


with open('cities.db', 'w') as file, open('cities_as_dict.db', 'w') as file2:
    file2.write('{' + '\n')
    for i in range(1, 4119):
        ignored = [1440, 3875, 367]  # UTC, Zulu, Kyiv
        ignored.extend(range(3878, 3902))  # Alpha, Beta, etc.
        ignored.extend(range(3903, 3929))  # UTC times
        if i in ignored:
            continue
        line = get_city_id(i)
        if line:
            print('Updating : ' + line)
            line2 = line.split('=')
            file.write(line + '\n')
            file2.write("'" + line2[0] + "':'" + line2[1] + "'" + '\n')
    file2.write('}' + '\n')
print(os.getcwd())
print('finished')
