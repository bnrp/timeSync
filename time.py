from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, random

url = "https://www.timeanddate.com/worldclock/usa/philadelphia"
page = urlopen(url)

dattime = BeautifulSoup(page, "html.parser")

#TIME

webtime = dattime.find(id="ct").string
webtimear = webtime.split(" ")

time = webtimear[0].split(":")

ampm = webtimear[1]

hourampm = time[0]
if ampm == "am":
    if hourampm == 12:
        hour = "0" + (hourampm - 12)
    else:
        if int(hourampm) <= 9:
            hour = "0" + hourampm
        else:
            hour = hourampm
elif ampm == "pm":
    if hourampm == 12:
        hour = hourampm
    else:
        hour = int(hourampm) + 12
else:
    exit()

minute = time[1]
second = time[2]

# DATE

webdate = dattime.find(id="ctdat").string
webdate = webdate.replace(",", "")
webdatear = webdate.split(" ")

date = webdatear[1:4]

weekday = webdatear[0]

monthname = date[0]
if monthname == "January":
    month = "01"
elif monthname == "February":
    month = "02"
elif monthname == "March":
    month = "03"
elif monthname == "April":
    month = "04"
elif monthname == "May":
    month = "05"
elif monthname == "June":
    month = "06"
elif monthname == "July":
    month = "07"
elif monthname == "August":
    month = "08"
elif monthname == "September":
    month = "09"
elif monthname == "October":
    month = "10"
elif monthname == "November":
    month = "11"
elif monthname == "December":
    month = "12"
else:
    month = 0

year = date[2]

dayz = date[1]
if int(dayz) <= 9:
    day = "0" + dayz
else:
    day = dayz

# SETTING SYSTEM CLOCK

if not month == 0:
    execute = open("time.bat", "w+")
    execute.write("date " + str(month) + "-" + str(day) + "-" + str(year) + "\n" + "time " + str(hour) + ":" + str(minute) + ":" + str(second) + "\n" + "del %0")

    path = r"C:\Users\BenPC\timeSync"
    file = "runthetime.vbs"
    os.startfile(path+'\\'+file)
else:
    exit()