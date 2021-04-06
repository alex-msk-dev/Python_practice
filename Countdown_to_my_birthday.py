# Countdown to my birthday
import datetime

now = datetime.datetime.today() #Cегодняшний день
bd = datetime.datetime(2021, 8, 6) #Дата дня рождения
d = bd - now #Для подсчёта дней нужно отнять от даты дня рождения, сегодняшнюю дату
print('До дня рождения: {} дня/дней.'.format(d.days)) #Вывод колличества дней