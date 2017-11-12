from datetime import date
import calendar

def meetup_day(year, month, day_of_the_week, which):
    if day_of_the_week == 'Monday':
        day_of_the_week = 1
    print (calendar.weekday(year, month, day_of_the_week))





meetup_day(2013, 5, 'Monday', 'teenth')
#antwoord is 13 mei
week_days = [x for x in calendar.day_name]
# print(week_days)
# print(calendar.monthcalendar(2013, 5))
# print(calendar.monthcalendar(2013, 6))
month = calendar.monthcalendar(2013, 5)

def monthDayName(month):
    day_week_name = []
    for week in month:
        for week_day in week:
            if week_day != 0:

                month_day = week_day
                month_day_index = week_days[week.index(week_day)]
                day_week_name.append([week_day, month_day_index])
    return day_week_name


print(monthDayName(month))