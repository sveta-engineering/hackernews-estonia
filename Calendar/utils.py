from datetime import datetime, timedelta, date
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        
        return '<td></td>'
    
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'
    
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        # cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        # format string to mark current date
        print('self.month: ', self.month)
        print('datetime.now', datetime.now().month)
        if (self.month == datetime.now().month):
            print(cal)
            today = date.today()
            today = today.strftime("%d")
            today = today.lstrip("0") # remove leading zero
            result = cal.find(today)
            new_cal_2 = cal[result-6:result-2].replace("date", "tday")
            new_cal_1 = cal[:result-6]
            new_cal_3 = cal[result-2:]
            new_cal = new_cal_1+new_cal_2+new_cal_3
            return new_cal
        return cal


