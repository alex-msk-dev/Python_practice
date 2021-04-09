# My birthday
import datetime

now = datetime.datetime.today()
month = now.month

if now.day == 6 and now.month == 8: #Если сегодня эта дата, то это мой день рождения
    print("День моего рождения")

else: #Если дата другая, то не мой день рождения
    print("Не мой день рождения")