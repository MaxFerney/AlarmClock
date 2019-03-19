#####IMPORTS#####
import time
import webbrowser

#####SONG LINKS#####
finish_him = "https://www.youtube.com/watch?v=lCCESmq9-vs"
Anime = "https://www.youtube.com/watch?v=3YPRGVIX5TM"
MotionRide_Metal = "https://www.youtube.com/watch?v=JSYmw8HPWoU"
MotionRide_WhatHappened = "https://www.youtube.com/watch?v=PTQCK1Lmq2Q"

#####GLOBAL VARIABLES#####
global currenttime
currenttime= str(time.asctime())

#####WEBSITE VARIABLE#####
site = MotionRide_WhatHappened

#####ALARM TIME#####
#setTime = '### mar 19 08:15:00'

def alarmClock(setTime):
    currenttime = str(time.asctime())
    print("        ---------------------------------\n\tAlarm Set for "+setTime+"\n        ---------------------------------")
    while int(setTime[8:10]) >= int(currenttime[8:10]):
        if int(setTime[8:10]) <= int(currenttime[8:10]) and \
           int(setTime[11:13]) <= int(currenttime[11:13]) and \
           int(setTime[14:16]) <= int(currenttime[14:16]):
            break
        time.sleep(.5)
        currenttime = str(time.asctime())
        
    print("loop broken! ALARM GOING OFF!")
    time.sleep(1)

    webbrowser.open(site,0,True)    
    

def setAlarm():
    setTime = 'day mth 00 00:00:00'
    day = input('input day of month. (if last day of month, add 1 to last day. if no input, then tommorrow will be assumed): \n\t')
    if day == '':
        day = str(int(currenttime[8:10])+1)
        if len(str(day)) == 1:
            day = '0'+str(day)
    elif len(str(day)) == 1:
        day = '0'+str(day)
    hour = input('input hour (24 hour format): \n\t')
    if hour == '':
        hour = '08'
    elif len(hour) == 1:
        hour = '0'+hour
    minute = input('input minute: \n\t')
    if minute == '':
        minute = '00'
    elif len(minute) == 1:
        minute = '0'+minute
    second = input('input second: \n\t')
    if second == '':
        second = '00'
    elif len(second)==1:
        second = '0'+second

    setTime = '        '+day+' '+hour+':'+minute+':'+second
    alarmClock(setTime)



#alarmClock(setAlarm())
setAlarm()
print("\nTo access alarm again, type setAlarm()")
