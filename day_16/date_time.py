from datetime import datetime

now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day + month + year + hour + minute + timestamp)

t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)

today = datetime(2019, 12, 5)
today_time = today.strftime("%d/%m/%Y")
print(today_time)

new_year = datetime(2023, 12, 31)
difference = new_year - now
print(f"It will take another {difference.days} days to new year")

start_date = datetime(year=1970, day=1, month=1)
now_timedelta = datetime(year=2023, month=3, day=23)
until_now = now_timedelta - start_date
print(f"There were {until_now.days} days since {start_date.day}/{start_date.month}/{start_date.year}")

"""
Validate underage based on date of birth
Timestamp on logs
Check expiration date
"""
