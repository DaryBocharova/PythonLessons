'''
Напечатайте в консоль даты: вчера, сегодня, месяц назад
Превратите строку "01/01/17 12:10:03.234567" в объект datetime
'''

from datetime import datetime, date, timedelta


dt_now = date.today()
delta = timedelta(days=1)
delta1 = timedelta(days=30)

str_dt = '01/01/17 12:10:03.234567'




print(dt_now)
print(dt_now - delta)
print(dt_now - delta1)
print(datetime.strptime(str_dt, '%m/%d/%y %H:%M:%S.%f'))

