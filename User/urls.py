from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('user/<username>', UserInfoView, name='user_info'),
    path('posts/<username>',UserSubmissions, name='user_posts'),
    path('submissions/<username>',UserAllSubmissions, name='user_submissions'),
    path('comments/<username>', UserCommentSubmissions, name='user_comments'),
    path("events/<username>", UserEventSubmissions, name="user_events"),
    path("jobs/<username>", UserJobSubmissions, name="user_jobs"),
    path('upvoted/<username>',UserUpvotes, name='user_upvotes'),
    path('signin',UserSigninView, name='signin'),
    path('signup',UserSignupView, name='signup'),
    path('signout',UserSignoutView, name='signout'),
]