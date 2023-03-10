
import datetime
import time
import winsound

invalid = True

while(invalid):
# Get a valid user input for the alarm time
    print("Set a valid time for the alarm (Ex. 06:30)")
    userInput = input(">> ")

# For example, this will convert 6:30 to an array of [6, 30].
    alarmTime = [int(n) for n in userInput.split(":")]

# Validate the time entered to be between 0 and 24 (hours) or 0 and 60 (minutes)
    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    elif alarmTime[1] >= 60 or alarmTime[1] < 0:
        invalid = True
    else:
        invalid = False

# Number of seconds in an Hour, Minute, and Second
seconds_hms = [3600, 60, 1]

# Convert the alarm time to seconds
alarmSeconds = sum([a * b for a, b in zip(seconds_hms[:len(alarmTime)], alarmTime)])
now = datetime.datetime.now()
currentTimeInSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
secondsUntilAlarm = alarmSeconds - currentTimeInSeconds
if secondsUntilAlarm < 0:
    secondsUntilAlarm += 86400 # number of seconds in a day

print("Alarm is set!")
print("The alarm will ring after %s" % datetime.timedelta(seconds=secondsUntilAlarm))
