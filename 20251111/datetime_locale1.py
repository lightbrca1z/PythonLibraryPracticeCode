import locale
import datetime
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
dt = datetime.datetime(2022, 11, 5, 15, 5, 10)
print(dt.strftime('%A'))
print(dt.strftime('%a'))