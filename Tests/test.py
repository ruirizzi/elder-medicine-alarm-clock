from enum import Enum
import time
import datetime
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
sched = Schedule(WeekDays.FRIDAY.value, 10, 39)
schedList.append(sched)
sched = Schedule(WeekDays.FRIDAY.value, 10, 38)
schedList.append(sched)
sched = Schedule(WeekDays.FRIDAY.value, 10, 40)
schedList.append(sched)

while True:
    time.sleep(5)
    now = datetime.datetime.today()
    for s in schedList:
        if s.dayOfWeek == now.weekday() and s.hour == now.hour and s.minute ==  now.minute:
            pass