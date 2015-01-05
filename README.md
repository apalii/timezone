# Timezone converter

Another useful script which helps in day-to-day routine.
(it takes all data from `timeanddate.com`)


### What should be installed : 

1) Of course Python3

2) Script:

```bash
wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/apalii/timezone/master/timezone.py
```

3) ALso you need `pip` for python3 - it is command line tool which can install/update/uninstall Python packages.

```bash
sudo apt-get install python3-pip 
```

4) Requests module 

```bash
sudo pip3 install requests
```
5) beautifulsoup4 module

```bash
sudo pip3 install beautifulsoup4
```

On my machine:

```bash
echo -e "$(python -V)$(python3 -V)\n$(pip list|egrep -i 'req|beau|argp')"
````

* Python 2.7.6
* Python 3.4.0
* argparse (1.2.1)
* beautifulsoup4 (4.3.2)
* requests (2.2.1)


### Example :

Usecase : 
You should schedule some maintenance on the production installation in different time zone.
Solution:
Let's imagine that some restarts should be performed on 5th of Dec at 23-00 (New-York TZ).
So run the following:

```bash
python3 timezone.py -c new-york -d 20141205 -t 23

where 
   -c - city
   -d - date in format yyymmdd
   -t - time hhmmss
```

Output will be the following (just copy/paste in TT): 
```
http://www.timeanddate.com/worldclock/converted.html?iso=20141205T23&p1=179&p2=367

New York (U.S.A. - New York) Friday, December 5, 2014 at 11:00:00 PM EST
Kyiv (Ukraine) Saturday, December 6, 2014 at 6:00:00 AM EET
Corresponding UTC (GMT) Saturday, December 6, 2014 at 04:00:00
```
## Details

### Usage :

```
usage: timezone.py [-h] --date DATE --time TIME --city CITY [--debug]

Timezone converter beta version

optional arguments:
  -h, --help            show this help message and exit
  --date DATE, -d DATE  Example: -d 20141201
  --time TIME, -t TIME  Example: -t 23 - it means 23:00:00
  --city CITY, -c CITY  Example: -c new-york
  --debug               Debug

```

And then, using requests and bs4, creates a list with needed data :

```python
In [22]: for i in soup.find_all('td'):
   ....:     print i.text
   ....:     
Sydney (Australia - New South Wales)
Monday, December 1, 2014 at 11:00:00 PM
AEDT
UTC+11 hours
Kyiv (Ukraine)
Monday, December 1, 2014 at 2:00:00 PM
EET
UTC+2 hours
Corresponding UTC (GMT)
Monday, December 1, 2014 at 12:00:00
```

# updatedb script

If you run it you will download 4119 pages from timeanddate.com
and create new databases with IDs of the cities. Some unusefull 
cities will be skipped :
```python
ignored = [1440, 3875, 367] # UTC, Zulu, Kyiv
ignored.extend(range(3878, 3902)) # Alpha, Beta, etc.
ignored.extend(range(3903, 3929)) # UTC times
if i in ignored:
    continue
```
It takes about 2 hours (:
