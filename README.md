Timezone converter
==================

Another useful script which helps in day-to-day routine.
Data from timeanddate.com

Example :
---------

Usecase : 
Schedule some maintenance on the production installation in different time zone.
Solution:
Let's imagine that some restarts should be performed on 5th of Dec at 23-00 (New-York TZ).
So 
> python timezone.py -c new-york -d 20141205 -t 23
Output will be the following : 

New York (U.S.A. - New York) Friday, December 5, 2014 at 11:00:00 PM EST UTC-5 hours
Kyiv (Ukraine) Saturday, December 6, 2014 at 6:00:00 AM EET UTC+2 hours
Corresponding UTC (GMT) Saturday, December 6, 2014 at 04:00:00 


What should be installed : 
--------------------------

1) Of course Python (:

2) Script and cities database
> wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/apalii/timezone/master/timezone.py
> wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/apalii/timezone/master/cities.db

3) pip - command line tool which can install/update/uninstall Python packages.

> sudo apt-get install python-pip   or  $ sudo yum install python-pip 

4) Requests module 
> sudo pip install requests

5) beautifulsoup4 module
> sudo pip install beautifulsoup4

--------------------------
On my machine:

> echo -e "$(python -V)$(python3 -V)\n$(pip list|egrep -i 'req|beau|argp')"
Python 2.7.6
Python 3.4.0
argparse (1.2.1)
beautifulsoup4 (4.3.2)
requests (2.2.1)
