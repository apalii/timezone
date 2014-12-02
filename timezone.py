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
   $ python timezone.py -c new_york -d 20141205 -t 23
   
   Date format : yyyymmdd
   Time format : hh
   Use underscore insted space in city names ! 
  ''')

parser.add_argument("--date", "-d", type=str, help="Example: -d 20141201")
parser.add_argument("--time", "-t", type=str, help="Example: -t 23   - it means 23:00")
parser.add_argument("--city", "-c", type=str, help="Example: -c new_york ")
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
            for line in db:
                if line.startswith(city):
                    return line[len(city) + 1:]
                    break
    except IOError, e:
        print 'Can not open the file !'
        sys.exit(1)


def get_timezone(date, hour, city):

    # http://www.timeanddate.com/worldclock/converted.html?iso=20141201T23&p1=240&p2=367
    base_url = 'http://www.timeanddate.com/worldclock/converted.html'
    params = '?iso={}T{}&p1={}&p2=367'.format(date,hour,city)
     
    data = r.get(base_url + params).text
    soup = bs(data)
    time = []
     
    for i in soup.find_all('td'):
        time.append(''.join(i.text))
     
    print time[0], time[1], time[2], time[3]
    print time[4], time[5], time[6], time[7]
    print time[8], time[9], time[10] + '\n'


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print 'Use --help for more detail'
    else:
        city_id = get_city_id(pargs.city)
        if city_id:
            get_timezone(pargs.date, pargs.time, city_id)
        else:
            print('City - not found !')