from django.contrib import admin

from .models import Post, Comment, Vote, CommentVote

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(CommentVote)