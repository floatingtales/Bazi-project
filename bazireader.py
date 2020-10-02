import json

#imports json data from bazi-scrapper, and takes in arguments for bazi to extract that data
bazidata = {}
with open('Bazi-scrapper/bazi.json') as Bazijson:
    bazidata = json.load(Bazijson)

def leapyears(year):
    return None

def bazivalues(year,month,date):
    return bazidata[year][month][date]

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
