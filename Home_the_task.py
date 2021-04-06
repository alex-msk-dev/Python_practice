# My birthday
import datetime

now = datetime.datetime.today()
month = now.month
year = now.year

if now.day == 6 and now.month == 8 and now.year == 2021: #Если сегодня эта дата, то это мой день рождения
    print("День моего рождения")
    exit(1)

else: #Если дата другая, то не мой день рождения
    print("Не мой день рождения")