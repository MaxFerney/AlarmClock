import time
import webbrowser


finish_him = "https://www.youtube.com/watch?v=lCCESmq9-vs"
Anime = "https://www.youtube.com/watch?v=3YPRGVIX5TM"
MotionRide = "https://www.youtube.com/watch?v=JSYmw8HPWoU"


#####WEBSITE VARIABLE#####
site = MotionRide

#####ALARM TIME#####
setTime = 'thu jan 31 08:00:00'


currenttime = str(time.asctime())
print(setTime)
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
    
      

