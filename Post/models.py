from django.db import models

from django.contrib.auth.models import User

from datetime import datetime
import pytz

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80, unique=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    url = models.URLField("URL", max_length=256, blank=False)
    domain = models.CharField(max_length=50, blank=False)
    votes = models.IntegerField(null=True)
    score = models.FloatField(null=True)
    comments = models.IntegerField(null=True)

    def __unicode__(self):
        return self.title
    
    def count_votes(self):
        self.votes = Vote.objects.filter(post=self).count()

    def count_comments(self):
        self.comments = Comment.objects.filter(post=self).count()
    
    def calculate_score(self):
        tallinn_tz = pytz.timezone("Europe/Tallinn")
        now = datetime.now(tallinn_tz)
        duration = now - self.created_on
        item_hour_age = duration.total_seconds() / 3600
        gravity = 1.8
        self.score = (self.votes+1)/pow((item_hour_age+2), gravity)
        self.save()

class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    votes = models.IntegerField(null=True)
    content = models.TextField()
    identifier = models.IntegerField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    def __unicode__(self):
        return f"Comment by {self.user.username}"
    
    def count_votes(self):
        self.votes = CommentVote.objects.filter(comment=self).count()
        self.save()

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __unicode__(self):
        return f"{self.user.username} upvoted {self.link.title}"

class CommentVote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __unicode__(self):
        return f"{self.user.username} upvoted {self.link.title}"