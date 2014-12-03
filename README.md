# Timezone converter

Another useful script which helps in day-to-day routine.
Data from timeanddate.com


### What should be installed : 

1) Of course Python (:

2) Script and cities database:

```bash
wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/apalii/timezone/master/timezone.py
wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/apalii/timezone/master/cities.db
```

3) pip - command line tool which can install/update/uninstall Python packages.

```bash
sudo apt-get install python-pip   or  $ sudo yum install python-pip 
```

4) Requests module 

```bash
sudo pip install requests
```
5) beautifulsoup4 module

```bash
sudo pip install beautifulsoup4
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
python timezone.py -c new-york -d 20141205 -t 23
```

Output will be the following : 
```
New York (U.S.A. - New York) Friday, December 5, 2014 at 11:00:00 PM EST UTC-5 hours
Kyiv (Ukraine) Saturday, December 6, 2014 at 6:00:00 AM EET UTC+2 hours
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

Script just takes an id of the city from the cities.db file 

```python
with open('cities.db') as db:
    city_pattern = re.compile(city + '=')
    for line in db:
        if re.search(city_pattern, line.rstrip()):
            return line.rstrip().split('=')[1]]
```

DB (just text file) consist of `city=city_id` data :

```bash
...
niagara-falls=1189
nha-trang=4069
new-york=179
new-westminster=111
...
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
