#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import re
import sys
import time
try :
    from bs4 import BeautifulSoup as bs
    import requests as r
    import argparse
except ImportError:
    print('Please install requests, bs4 and argparse modules')
    sys.exit(1)
 
parser = argparse.ArgumentParser(description="Timezone converter beta version",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''Examples:
   $ python timezone.py -c new-york -d 20141205 -t 2330

   Date format : yyyymmdd
   Time format : hhmmss 
  ''')

parser.add_argument("--date", "-d", type=str, required=True, help="Example: -d 20141201")
parser.add_argument("--time", "-t", type=str, required=True, help="Example: -t 23  - it means 23:00:00")
parser.add_argument("--city", "-c", type=str, required=True, help="Example: -c new-york ")
parser.add_argument("--debug", action='store_true', help="Debug")
pargs = parser.parse_args()
if pargs.debug:
    print(pargs)

def timer(wrapped):
    def inner(*args, **kwargs):
        before = time.time()
        ret = wrapped(*args, **kwargs)
        if pargs.debug:
            print("get_city_id() executed in {0:f} seconds".format(time.time() - before))
        return ret 
    return inner


@timer
def get_city_id(city):
    try:
        with open('cities.db') as db:
            city_pattern = re.compile(city + '=', re.I)
            for line in db:
                if re.search(city_pattern, line.rstrip()):
                    return line.rstrip().split('=')[1]
                    break
    except IOError as e:
        print('Can not open cities.db file !')
        sys.exit(1)


def get_timezone(date, hour, city):
    base_url = 'http://www.timeanddate.com/worldclock/converted.html'
    params = '?iso={}T{}&p1={}&p2=367'.format(date,hour,city)
    headers = {'Accept-Language':'en-US,en;q=0.5'}
    data = r.get(base_url + params, headers=headers).text
    soup = bs(data)
    time = []
    
    for i in soup.find_all('td'):
        time.append(''.join(i.text))
    if pargs.debug:
        print('\n',time)
    print('\n{}\n'.format(base_url + params))
    print(' '.join(time[:3]))
    print(' '.join(time[4:7]))
    print(' '.join(time[8:10]) + '\n')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Use --help for more detail')
    else:
        city_id = get_city_id(pargs.city)
        if city_id and city_id != '367':
            get_timezone(pargs.date[:8], pargs.time[:6], city_id)
        else:
            print('City - not found !')
