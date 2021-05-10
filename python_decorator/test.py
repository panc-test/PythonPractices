import datetime

time = datetime.datetime.now()
print(time)
print(str(time).split(".")[0])
print(time.strftime("%Y-%m-%d %H:%M:%S"))


