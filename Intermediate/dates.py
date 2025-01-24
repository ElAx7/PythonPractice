##Dates 

from datetime import datetime

now = datetime.now() 

def print_date(date):
    print (now.year)
    print (now.month)
    print (now.day)
    print (now.hour)
    print (now.minute)
    print (now.second)
    print(date.timestamp())

print_date(now)

year_2025 = datetime(2025, 1, 1)

print_date(year_2025)

from datetime import time

current_time = time(21, 6, 0 ) #time is empty by default

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year + 1, current_date.month, current_date.day)

print(current_date.year)

diff = year_2025 - now
print(diff)

diff = year_2025.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(days = 1, hours = 2, minutes = 30 )
end_timedelta = timedelta(days = 2, hours = 4, minutes = 60 )
print(start_timedelta - end_timedelta)
print(start_timedelta + end_timedelta)
