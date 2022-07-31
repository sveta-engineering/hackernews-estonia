from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', PostListView, name='home'),
    path('submit', PostSubmitView, name='submit'),
    path('edit/<int:id>', PostEditView, name='edit'),
    path('post/<int:id>',CommentListView, name='post'),
    path('commentedit/<int:id>', CommentEditView, name='commentedit'),
    path('post/<int:id1>/comment/<int:id2>',CommentReplyView,name='reply'),
    path('vote/<int:id>',VoteUpView,name='vote'),
    path('commentvote/<int:id>',CommentVoteUpView,name='commentvote'),
]