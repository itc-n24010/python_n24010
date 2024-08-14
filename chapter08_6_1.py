from datetime import datetime
time = '20180101120130'
a = datetime.strptime(time, "%Y%m%d%H%M%S")
print(a)
print(a.strftime("%Y%m%d%H%M%S"))
