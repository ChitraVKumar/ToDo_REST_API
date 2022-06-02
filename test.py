import datetime
test = lambda s: datetime.datetime.strptime(s,"%d/%m/%Y %H:%M:%S")

print(test("12/11/2018 09:15:32"))