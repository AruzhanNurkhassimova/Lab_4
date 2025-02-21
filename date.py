#1
from datetime import date,  timedelta, datetime
current = date.today() - timedelta(5)
print("Current time: ", date.today())
print("Substact five days : ",current)


#2
from datetime import date,  timedelta, datetime
yesterday = date.today()-timedelta(1)

print("Yesterday: ",yesterday)

today = date.today()

print("Today: ",today)

tomorrow = date.today()+timedelta(1)

print("Tomorrow: ", tomorrow)


#3
from datetime import date, timedelta, datetime
time = datetime.now()
without_microseconds = time.strftime("%Y-%m-%d, %H:%M:%S")
print(without_microseconds)


#4
from datetime import date, timedelta, datetime
yesterday = datetime.now() - timedelta(1)
today = datetime.now()

yesterday = datetime.timestamp(yesterday)
today = datetime.timestamp(today)

print(today - yesterday)