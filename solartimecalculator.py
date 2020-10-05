from datetime import datetime, date, time, timedelta
from calendar import isleap
from math import pi, sin, cos

def solartime(datetimetoconvert, tzoffset, lon):
    year = datetimetoconvert.year
    month = datetimetoconvert.month
    day = datetimetoconvert.day
    hour = datetimetoconvert.hour
    minutes = datetimetoconvert.minute
    seconds = datetimetoconvert.second
    dayindex = datetimetoconvert.timetuple().tm_yday

    gamma = None
    if isleap(year):
        gamma = 2 * pi /366 * (dayindex - 1 + ((hour-12) / 24))
    else:
        gamma = 2 * pi /365 * (dayindex - 1 + ((hour-12) / 24))

    eqtime = 229.18 * (0.000075 + (0.001868 * cos(gamma)) - (0.032077 * sin (gamma)) - (0.014615 * cos(2 * gamma)) - (0.040849 * sin(2 * gamma)))

    #time offset in minutes
    timeoffset = eqtime + (4*lon) - (60*tzoffset)

    #true solar time in minutes
    truesolartime = (hour*60) + minutes + (seconds/60) + timeoffset

    deltatime = timedelta(minutes = truesolartime)

    truesolarcalendar = datetime.combine(datetimetoconvert.date(), time(0)) + deltatime

    return truesolarcalendar
