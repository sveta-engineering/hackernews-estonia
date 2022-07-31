from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('jobs', JobPostListView, name='jobs'),
    path('jobdetail/<int:id>', JobPostDetailView, name='jobdetail'),
    path('jobsubmit', JobPostSubmitView, name='jobsubmit'),
    path('jobedit/<int:id>', JobPostEditView, name='jobedit'),
]