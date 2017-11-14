from datetime import date
import calendar


class MeetupDayException(Exception):
    pass


def group_week_days(year, month):
    '''returns all the same week days in one list'''
    month_cal = calendar.monthcalendar(year, month)
    # print(month_cal)
    week1 = month_cal[0]
    week2 = month_cal[1]
    week3 = month_cal[2]
    week4 = month_cal[3]
    week5 = month_cal[4]
    # zip to put together the mondays, tuesdays etc.
    # returns tuple
    # days = list(zip(week1, week2, week3, week4, week5))
    days = list(map(list, zip(*month_cal)))
    return days

print(group_week_days(2015, 5))
# print(calendar.monthcalendar(2013, 5))

def meetup_day(year, month, day_of_the_week, which):
    # month = calendar.monthcalendar(2013, 5)
    # MeetupDayException = "Invalid date"\
    last_day_of_month = calendar.monthrange(year, month)[1]
    # get the week day in a list
    week_days = [x for x in calendar.day_name]
    week_day_int = week_days.index(day_of_the_week)
    # get all day_of_the_week in month
    week_group = group_week_days(year, month)
    print("int", week_day_int)
    print("week group", week_group)

    for x in week_group[week_day_int]:
        if which == 'teenth':
            if x in range(13,20):
                return date(year, month, x)
        elif which == 'last':
            if last_day_of_month == 28:
                if x in range(22,29):
                    return date(year, month, x)
            elif last_day_of_month == 29:
                if x in range(23,30):
                    return date(year, month, x)
            elif last_day_of_month == 30:
                if x in range(24, 31):
                    return date(year, month, x)
            else:
                if x in range(25,32):
                    return date(year, month, x)
        elif which == '1st':
            if x in range(1, 8):
                return date(year, month, x)
        elif which == '2nd':
            if x in range(8, 15):
                return date(year, month, x)
        elif which == '3rd':
            if x in range(15, 22):
                return date(year, month, x)
        elif which == '4th':
            if x in range(22, 29):
                return date(year, month, x)
        elif which == '5th':
            if x in range(29, 32):
                if x  is None:
                    raise MeetupDayException()
                else:
                    return date(year, month, x)


#print(meetup_day(2013, 12, 'Friday', '1st'))
# 2013, 12, 6
#print(meetup_day(2017, 11, 'Wednesday', 'teenth'))
#print(calendar.monthcalendar(2013, 1))
# print(week_days)
#print(calendar.monthcalendar(2015, 3))
#print(meetup_day(2013, 5, 'Tuesday', '4th'))
print(meetup_day(2012, 2, 'Wednesday', 'last'))
print(meetup_day(2015, 2, 'Sunday', 'last'))
print(meetup_day(2015, 2, 'Monday', '5th'))