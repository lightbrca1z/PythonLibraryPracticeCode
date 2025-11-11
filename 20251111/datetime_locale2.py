import locale
import datetime

dt = datetime.datetime(2022, 11, 5, 15, 5, 10)
td = datetime.timedelta(days=30, hours=4)
print(dt + td)