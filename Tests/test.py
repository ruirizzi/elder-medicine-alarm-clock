from enum import Enum
import time
import datetime
import threading

class Schedule():
    def __init__(self, dayOfWeek, hour, minute):
        self.dayOfWeek = dayOfWeek
        self.hour = hour
        self.minute = minute


class WeekDays(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

schedList = []
sched = Schedule(WeekDays.FRIDAY, 11, 14)
schedList.append(sched)
sched = Schedule(WeekDays.FRIDAY, 11, 13)
schedList.append(sched)
sched = Schedule(WeekDays.FRIDAY, 11, 12)
schedList.append(sched)

while True:
    now = datetime.datetime.today()
    for s in schedList:
        if s.dayOfWeek.value == now.weekday() and s.hour == now.hour and s.minute ==  now.minute:
            minute, hour = "00"
            
            if (s.minute < 10):
                minute = "0"
            else:
                minute = ""

            if(s.hour < 10):
                hour = "0"
            else:
                hour = ""


            print("Schedule Hit: {}, {}{}:{}{}".format(s.dayOfWeek.name, hour, s.hour, minute, s.minute))
    time.sleep(60)
