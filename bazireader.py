import json
from calendar import isleap
from datetime import datetime, date, time, timedelta
from solartimecalculator import solartime

#imports json data from bazi-scrapper, and takes in arguments for bazi to extract that data
bazidata = {}
with open('Bazi-scrapper/bazi.json') as Bazijson:
    bazidata = json.load(Bazijson)

def hourcycle(cyclestart, time):
    #bazi dates starts and ends at 11pm solar time
    HShour = None
    EBhour = None

    if time.hour >= 23 or time.hour < 1:
        HShour = cyclestart
        EBhour = 1
    elif time.hour >= 1 and time.hour < 3:
        HShour = cyclestart + 1
        EBhour = 2
    elif time.hour >= 3 and time.hour < 5:
        HShour = cyclestart + 2
        EBhour = 3
    elif time.hour >= 5 and time.hour < 7:
        HShour = cyclestart + 3
        EBhour = 4
    elif time.hour >= 7 and time.hour < 9:
        HShour = cyclestart + 4
        EBhour = 5
    elif time.hour >= 9 and time.hour < 11:
        HShour = cyclestart + 5
        EBhour = 6
    elif time.hour >= 11 and time.hour < 13:
        HShour = cyclestart + 6
        EBhour = 7
    elif time.hour >=13 and time.hour < 15:
        HShour = cyclestart + 7
        EBhour = 8
    elif time.hour >= 15 and time.hour < 17:
        HShour = cyclestart + 8
        EBhour = 9
    elif time.hour >= 17 and time.hour < 19:
        HShour = cyclestart + 9
        EBhour = 10
    elif time.hour >= 19 and time.hour < 21:
        HShour = cyclestart + 10
        EBhour = 11
    elif time.hour >= 21 and time.hour < 23:
        HShour = cyclestart + 11
        EBhour = 12

    #adjusted for shift of 1 in systems
    HShour = HShour%10  + 1

    #returns the non-adjusted Heavenly Stem (1 for zi, 2 for chou, etc)
    return HShour, EBhour

def bazivalues(bazidt):

    #day rolled over after 11 pm
    if bazidt.hour >= 23:
        year, month, day = str(bazidt.year), str(bazidt.month), str(bazidt.day + 1)
    else:
        year, month, day = str(bazidt.year), str(bazidt.month), str(bazidt.day)

    #shifts the HS back by a single value (0 for zi, 1 for chou, etc)
    HShourpointer = 0

    for years in range(1901, int(year)):
        if isleap(years):
            HShourpointer = HShourpointer + 2

    #day rolled over after 11 pm
    if bazidt.hour >= 23:
        dayindex = bazidt.timetuple().tm_yday + 1
    else:
        dayindex = bazidt.timetuple().tm_yday

    for index in range(1, dayindex):
        HShourpointer = HShourpointer + 2

    #still shifting HS by 1, do hourcycle first and then add 1 to it
    HShourpointer = HShourpointer%10

    bazichart = bazidata[year][month][day]

    bazichart['HSHour'], bazichart['EBHour'] = hourcycle(HShourpointer, bazidt)

    return bazichart

def bazireader(bazidict):

    indicator = 0

    switches = {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None
    }

    for key in bazidict:
        switches[indicator] = bazidict[key]
        indicator = indicator + 1

    idx = switches[0]
    Syear = switches[1]
    Smonth = switches[2]
    Sday = switches[3]
    HSyear = switches[4]
    EByear = switches[5]
    HSmonth = switches[6]
    EBmonth = switches[7]
    HSday = switches[8]
    EBday = switches[9]
    Season = switches[10]
    HShour = switches[11]
    EBhour = switches[12]

    print(HSyear, EByear, HSmonth, EBmonth, HSday, EBday, HShour, EBhour)

readdate = datetime(1996, 8 , 4, 14, 0, 0, 0)
tzoffset = 8
longitude = 121.0437

solarreaddate = solartime(readdate, tzoffset, longitude)

print(solarreaddate)

bazireader(bazivalues(solarreaddate))
