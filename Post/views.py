from django.shortcuts import render, redirect, get_object_or_404
from urllib.parse import urlparse

from datetime import datetime
from .models import Post, Comment, Vote, CommentVote
from .forms import PostForm, CommentForm

# Create your views here.

################# POST ################################

def PostListView(request):
    posts = Post.objects.all().order_by('-score')
    for post in posts:
        post.count_votes()
        post.count_comments()
        post.calculate_score()

    context = {
        'posts': posts,
    }
    return render(request, 'Post/postlist.html', context)

def PostSubmitView(request):
    if request.user.is_authenticated:
        form = PostForm()
    
        if request.method == "POST":
            form = PostForm(request.POST)

            if form.is_valid():
                title = form.cleaned_data['title']
                url = form.cleaned_data['url']
                domain = urlparse(form.cleaned_data['url'])[1]
                creator = request.user
                created_on = datetime.now()

                post = Post(title=title, url=url, domain=domain,creator = creator, created_on=created_on)
                post.save()
                return redirect('/')
        return render(request, 'Post/submit.html', {'form': form})
    return redirect('User/signin')

def PostEditView(request, id):
    post = get_object_or_404(Post, id=id)
    if (post.creator == request.user):
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = PostForm(instance=post)
        return render(request, 'Post/submit.html', {'form': form})
    return redirect('/')

################# COMMENT ################################

def CommentListView(request, id):
    form = CommentForm()
    post = Post.objects.get(id=id)
    post.count_votes()
    post.count_comments()

    comments = []
    def func(i, parent):
        children = Comment.objects.filter(post=post).filter(identifier =i).filter(parent=parent).order_by('votes')
        for child in children:
            gchildren = Comment.objects.filter(post =post).filter(identifier = i+1).filter(parent=child)
            if len(gchildren)==0:
                comments.append(child)
            else:
                func(i+1,child)
                comments.append(child)
    func(0,None)

    for comment in comments:
        comment.count_votes()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data['content']
                comment = Comment(creator = request.user,post = post,content = content,identifier =0)
                comment.save()
                return redirect(f'/post/{id}')
        return redirect('/signin')

    context ={
        'form': form,
        'post': post,
        'comments': list(reversed(comments)),
    }
    return render(request,'Comment/commentpost.html', context)

def CommentEditView(request, id):
    comment = get_object_or_404(Comment, id=id)
    if (comment.creator == request.user):
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid:
                form.save()
                return redirect('/')
        form = CommentForm(instance=comment)
        return render(request, 'Comment/reply_post.html', {'form': form})
    return redirect('User/signin')

def CommentReplyView(request, id1, id2):
    form = CommentForm()
    comment = Comment.objects.get(id=id2)
    post = Post.objects.get(id=id1)

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
             
            if form.is_valid():
                reply_comment_content = form.cleaned_data['content']
                identifier = int(comment.identifier + 1)
 
                reply_comment = Comment(creator = request.user, post = post, content = reply_comment_content, parent=comment, identifier= identifier)
                reply_comment.save()
 
                return redirect(f'/post/{id1}')
        return redirect('/signin')
     
    context ={
        'form': form,
        'post': post,
        'comment': comment,
    }
    return render(request,'Comment/reply_post.html', context)

################## VOTE ##############################

def VoteUpView(request, id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=id)
        votes = Vote.objects.filter(post = post)
        v = votes.filter(voter = request.user)
        if len(v) == 0:
            upvote = Vote(voter=request.user, post=post)
            upvote.save()
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('/signin')

def CommentVoteUpView(request, id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=id)
        votes = CommentVote.objects.filter(comment = comment)
        v = votes.filter(voter = request.user)
        if len(v) == 0:
            upvote = CommentVote(voter=request.user, comment=comment)
            upvote.save()
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('/signin')