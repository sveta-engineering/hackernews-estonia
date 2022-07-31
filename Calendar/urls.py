from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('calendar', CalendarView.as_view(), name='calendar'),
    path("eventsubmit", EventSubmitView, name="event_submit"),
    path('eventdetail/<int:id>', EventDetailView, name='event_detail'),
    path('eventedit/<int:id>', EventEditView, name='event_edit'),
]