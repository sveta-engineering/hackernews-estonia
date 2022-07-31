from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from Post.models import Post, Vote, CommentVote, Comment
from JobPost.models import JobPost
from Calendar.models import Event

# Create your views here.
def UserInfoView(request, username):
    user = User.objects.get(username=username)
    context = {'user': user,}
    return render(request, 'User/user_info.html', context)

def UserSubmissions(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(creator=user)
    for post in posts:
        post.count_votes()
        post.count_comments()
    return render(request, 'User/user_posts.html', {'posts': posts})

def UserAllSubmissions(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(creator=user)
    comments = Comment.objects.filter(creator=user)
    jobs = JobPost.objects.filter(creator=user)
    events = Event.objects.filter(creator=user)
    return render(request, 'User/user_submissions.html', {'posts': posts, 'comments': comments, 'jobs': jobs, 'events': events})

def UserCommentSubmissions(request, username):
    user = User.objects.get(username=username)
    comments = Comment.objects.filter(creator=user)
    return render(request, 'User/user_comments.html', {'comments': comments})

def UserJobSubmissions(request, username):
    user = User.objects.get(username=username)
    jobs = JobPost.objects.filter(creator=user)
    return render(request, 'JobPost/user_jobs.html', {'jobs': jobs})

def UserEventSubmissions(request, username):
    user = User.objects.get(username=username)
    events = Event.objects.filter(creator=user)
    return render(request, 'User/user_events.html', {'events': events})

def UserUpvotes(request, username):
    user = User.objects.filter(username=username)
    news = Vote.objects.filter(voter=user[0])
    comments = CommentVote.objects.filter(voter=user[0])
    return render(request, 'User/upvoted.html', {'news': news, 'comments': comments})

def UserSignupView(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/')
        
        else:
            return render(request, 'User/auth_signup.html', {'form':form})
    
    else:
        form = UserCreationForm()
        return render(request, 'User/auth_signup.html', {'form':form})

def UserSigninView(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm()
            return render(request, 'User/auth_signin.html', {'form':form})

    else:
        form = AuthenticationForm()
        return render(request, 'User/auth_signin.html', {'form': form})
    
def UserSignoutView(request):
    logout(request)
    return redirect('/')