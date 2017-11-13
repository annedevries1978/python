from datetime import date
import calendar

def meetup_day(year, month, day_of_the_week, which):
    month = calendar.monthcalendar(2013, 5)
    # get the week day
    week_days = [x for x in calendar.day_name]
    for day_of_the_week in week_days:
        week_day_int = week_days.index(day_of_the_week)



meetup_day(2013, 5, 'Monday', 'teenth')
#antwoord is 13 mei
# print(week_days)
# print(calendar.monthcalendar(2013, 5))
month = calendar.monthcalendar(2013, 5)[1]
# month = calendar.monthrange(2013, 5)[1]
print(month)
