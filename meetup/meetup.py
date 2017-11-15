from datetime import date
import calendar


class MeetupDayException(Exception):
    pass


def group_week_days(year, month):
    '''returns all the same week days in one list'''
    month_cal = calendar.monthcalendar(year, month)
    days = list(map(list, zip(*month_cal)))
    return days

def meetup_day(year, month, day_of_the_week, which):
    last_day_of_month = calendar.monthrange(year, month)[1]
    # get the week day in a list
    week_days = [x for x in calendar.day_name]
    week_day_int = week_days.index(day_of_the_week)
    # get all day_of_the_week in month
    week_group = group_week_days(year, month)

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
                if x is None:
                    raise MeetupDayException()
                else:
                    return date(year, month, x)
