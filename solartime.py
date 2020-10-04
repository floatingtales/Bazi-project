import datetime
from calendar import isleap
from math import pi, sin, cos

def solartime(datetimetoconvert, offset, lat):
    year = datetimetoconvert
    month
    day
    dayindex
    hour

    gamma = None
    if isleap(solaryear):
        gamma = 2 * pi /366 * (dayindex - 1 + ((hour-12) / 24))
    else:
        gamma = 2 * pi /365 * (dayindex - 1 + ((hour-12) / 24))
