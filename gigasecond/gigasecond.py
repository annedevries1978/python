from _datetime import  datetime, timedelta

def add_gigasecond(birth_date):
    #import datetime
    return birth_date + timedelta(seconds=pow(10, 9))

print(add_gigasecond(datetime(1986, 4 ,4, 1, 7, 00)))