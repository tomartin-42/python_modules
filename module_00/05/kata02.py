from datetime import datetime
t = (3, 30, 2019, 9, 25)

time = datetime(t[2], t[3], t[4], t[0], t[1])
print(time.strftime("%m/%d/%Y %H:%M"))
