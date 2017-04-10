# Hint:  use Google to find python function

from datetime import datetime

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2 - d1).days)

print(days_between(date_start, date_stop))

####b)
date_start = '12312013'
date_stop = '05282015'

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m%d%Y")
    d2 = datetime.strptime(d2, "%m%d%Y")
    return abs((d2 - d1).days)

print(days_between(date_start, date_stop))

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d-%b-%Y")
    d2 = datetime.strptime(d2, "%d-%b-%Y")
    return abs((d2 - d1).days)

print(days_between(date_start, date_stop))
