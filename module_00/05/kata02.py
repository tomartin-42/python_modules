from datetime import datetime
t = (2019, 9, 25, 3, 30)

time = datetime(*t)
print(time.strftime("%m/%d/%Y %H:%M"))
