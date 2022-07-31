from tracemalloc import start
from django.shortcuts import get_object_or_404, render, redirect
import calendar
from .models import Event
from .forms import EventForm

# Create your views here.


from datetime import datetime, timedelta, date
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'Calendar/calendar.html'
    print("CalendarView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['current_month'] = get_month_name(cal.month)
        context['current_year'] = cal.year
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    print("prev_month")
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    print("next_month")
    return month

def get_month_name(n_month):
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return month_list[n_month]

def EventSubmitView(request):
    if request.user.is_authenticated:
        form = EventForm()

        if request.method == "POST":
            form = EventForm(request.POST)

            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                creator = request.user

                event = Event(creator=creator,title=title, description=description, start_time=start_time, end_time=end_time)
                event.save()
                return redirect('/')
        return render(request, 'Calendar/submit.html', {'form': form})
    return redirect('User/signin')
            
def EventDetailView(request, id):
    event = get_object_or_404(Event, id=id)
    context = {
        'event' : event,
    }
    return render(request, "Calendar/detail.html", context)

def EventEditView(request, id):
    event = get_object_or_404(Event, id=id)
    if (event.creator == request.user):
        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = EventForm(instance=event)
        return render(request, 'Calendar/submit.html', {'form': form})
    return redirect('/')