# Countdown to my birthday
from datetime import datetime

now = datetime.today() #Cегодняшний день
birth_month = 8
birth_day = 6
birthday_date = datetime(now.year, birth_month, birth_day) #Дата дня рождения
if (birthday_date < now):
	birthday_date = datetime(now.year + 1, birth_month, birth_day)
timedelta_for_birthday = birthday_date - now #Для подсчёта дней нужно отнять от даты дня рождения, сегодняшнюю дату
print('До дня рождения: {} дня/дней.'.format(timedelta_for_birthday.days)) #Вывод колличества дней