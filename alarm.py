
import time
import datetime
import winsound

invalid = True

while(invalid):

    #to get valid input from user
    print("set time(eg.6:30)")
    userinput = input(">>")

    #to convert given time to array eg. 6:30 to [6, 30]
    alarmTime = [int(n) for n in userinput.split(":")]

    #to validate entered time is hrs between 0 to 24 and min between 0 to 60
    if alarmTime[0]>=24 or alarmTime[0]<0:
        invalid= True
    if alarmTime[1]>=60 or alarmTime[1]<0:
        invalid= True

    else:
        invalid= False

#Number of seconds in hrs, min, second
seconds_hms = [3600,60,1]

#to convert alarm time to seconds

alarmSeconds = sum([a*b for a,b in zip (seconds_hms[:len(alarmTime)], alarmTime)])
now = datetime.datetime.now()
currentTimeinseconds = sum([a*b for a,b in zip (seconds_hms,[now.hour, now.minute, now.second])])
secondsUntilalarm= alarmSeconds-currentTimeinseconds
if secondsUntilalarm < 0:
    secondsUntilalarm += 86400

print("Alarm is set!")
print("The alarm will ring after %s" % datetime.timedelta(seconds=secondsUntilalarm))

#use time.sleep to wait till secondsUntilalarm
time.sleep(secondsUntilalarm)
print(f"{userinput}")
freq = 500
dur = 1000
winsound.Beep(freq, dur)