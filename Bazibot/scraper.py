import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://en.wikibooks.org/'
calendarurl = url + 'wiki/Ba_Zi/Hsia_Calendar'

print('retreiving:', calendarurl)

html = urllib.request.urlopen(calendarurl, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")
yearurl = re.findall('wiki/Ba_Zi/[0-9][0-9][0-9][0-9]' , str(soup('a')))

bazidict = {}

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


for year in yearurl:
    currentyearurl = url + str(year)

    print('Retreiving:', currentyearurl)

    html = urllib.request.urlopen(currentyearurl, context = ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tables = soup('td')

    #0 for index
    #1 for solar yr
    #2 for solar month
    #3 for solar day
    #4 for HS year
    #5 for EB year
    #6 for HS month
    #7 for EB month
    #8 for HS day
    #9 for EB day
    #10 for Season
    indicator = 0

    daydic = {}
    modic = {}

    monthflag = None

    for tablecontents in tables:
        switches[indicator] = int(re.findall('[0-9]+',str(tablecontents))[0])

        if indicator == 10:
            fulldic = {
            'idx': switches[0],
            'Syear': switches[1],
            'Smonth': switches[2],
            'Sday': switches[3],
            'HSyear': switches[4],
            'EByear': switches[5],
            'HSmonth': switches[6],
            'EBmonth': switches[7],
            'HSday': switches[8],
            'EBday': switches[9],
            'Season': switches[10]
            }

            if monthflag == None:
                monthflag = switches[2]
            elif monthflag != switches[2]:
                modic[monthflag] = daydic
                daydic = {}
                monthflag = switches[2]

            daydic[switches[3]] = fulldic

            if switches[3] == 31 and switches[2] == 12:
                modic[switches[2]] = daydic
                bazidict[switches[1]] = modic

        indicator = (indicator+1)%11

for year in bazidict:
    for month in bazidict[year]:
        for day in bazidict[year][month]:
            print('year', year)
            print('month', month)
            print('day', day)
            print('sequence', modic[month][day])

with open('bazi.json','w') as outfile:
    json.dump(bazidict, outfile)
