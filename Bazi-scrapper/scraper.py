import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import json

#scrapes data from wikibooks, to have it in a dictionary of bazi[year][month][date]

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
    10: None
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

with open('bazi.json','w') as outfile:
    json.dump(bazidict, outfile)

print("successfully scraped data and write it to json")
