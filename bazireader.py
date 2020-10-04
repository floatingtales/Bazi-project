import json
import calendar
import datetime

#imports json data from bazi-scrapper, and takes in arguments for bazi to extract that data
bazidata = {}
with open('Bazi-scrapper/bazi.json') as Bazijson:
    bazidata = json.load(Bazijson)

def bazivalues(year,month,day):

    #shifts all Heavenly stems by 1
    HShourpointer = 0

    for years in range(1901, int(year)):
        if calendar.isleap(years):
            HShourpointer = HShourpointer + 2

    #still shifting HS by 1, do hourcycle first and then add 1 to it
    HShourpointer = HShourpointer%10
    print ("starting at:",HShourpointer + 1)

    return bazidata[year][month][day]

def hourcycle(cyclestart, time):
    #bazi dates starts and ends at 11pm solar time
    HShour = None
    EBhour = None

    if time > 23 or time < 1:
        HShour = cyclestart
        EBhour = 1
    elif time >= 1 and time < 3:
        HShour = cyclestart + 1
        EBhour = 2
    elif time >= 3 and time < 5:
        HShour = cyclestart + 2
        EBhour = 3
    elif time >= 5 and time < 7:
        HShour = cyclestart + 3
        EBhour = 4
    elif time >= 7 and time < 9:
        HShour = cyclestart + 4
        EBhour = 5
    elif time >= 9 and time < 11:
        HShour = cyclestart + 5
        EBhour = 6
    elif time >= 11 and time < 13:
        HShour = cyclestart + 6
        EBhour = 7
    elif time >=13 and time < 15:
        HShour = cyclestart + 7
        EBhour = 8
    elif time >= 15 and time < 17:
        HShour = cyclestart + 8
        EBhour = 9
    elif time >= 17 and time < 19:
        HShour = cyclestart + 9
        EBhour = 10
    elif time >= 19 and time < 21:
        HShour = cyclestart + 10
        EBhour = 11
    elif time >= 21 and time < 23:
        HShour = cyclestart + 11
        EBhour = 12

    #adjusted for shift of 1 in systems
    HShour = HShour%10  + 1

    #returns the non-adjusted Heavenly Stem
    return HShour, EBhour

def bazireader(bazidict):

    idx = None
    Syear = None
    Smonth = None
    Sday = None
    HSyear = None
    EByear = None
    HSmonth = None
    EBmonth = None
    HSday = None
    EBday = None
    Season = None

    indicator = 0

    switches = {
        0: idx,
        1: Syear,
        2: Smonth,
        3: Sday,
        4: HSyear,
        5: EByear,
        6: HSmonth,
        7: EBmonth,
        8: HSday,
        9: EBday,
        10: Season
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

    print(HSyear, EByear, HSmonth, EBmonth)

bazireader(bazivalues('1996','8','4'))
