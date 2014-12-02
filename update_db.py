# Update cities DB
 
#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import re
import time
import sys
import os
try :
    from bs4 import BeautifulSoup as bs
    import requests as r
    import argparse
except ImportError:
    print('Please install requests/bs4/argparse modules')
    sys.exit(1)
 
 
def get_city_id(city_id):
    city_list, id_list = [], []
    id_patern = re.compile('meeting\.html\?p1=(\d{1,4})')
    url = 'http://www.timeanddate.com/worldclock/city.html?n=' + str(city_id)
    data = r.get(url).text
    time.sleep(1) # to avoid ban (:
    soup = bs(data)
    try:
        city = str(soup.find_all('title')).split('in')[1].strip().split(',')[0]
        city_list.append(city.lower().replace(' ', '_'))
        for i in soup.find_all('a'):
            match = re.search(id_patern, i.get('href'))
            if match:
                id_list.append(match.group(1))
                break
        city_ids_dict = dict(zip(city_list, id_list))
        for x,y in city_ids_dict.items(): 
            return x + '=' + y
    except IndexError, e:
        print(str(soup.find_all('title')))
        print('skipped due to {}'.format(e))
    finally:
        pass 
# try  IOError
with open('cities.db', 'a') as file, open('cities2.db', 'a') as file2:
    #file2.write('{' + '\n')
    for i in range(3728, 4119): #3728, 4119
        ignored = [1440, 3875] # UTC, Zulu
        ignored.extend(range(3878, 3902)) # Alpha, Beta, etc.
        ignored.extend(range(3903, 3929)) # UTC times
        if i in ignored:
            continue
        line = get_city_id(i)
        if line:
            print 'Updating : ' + line
            line2 = line.split('=')
            file.write(line + '\n')
            file2.write("'" + line2[0] + ':' + "'" + line2[1] + "'" + '\n' )
    file2.write('}' + '\n')
print os.getcwd()
print 'finished'
