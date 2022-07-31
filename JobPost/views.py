from django.shortcuts import get_object_or_404, redirect, render

from .models import JobPost
from .forms import JobPostForm
from datetime import datetime

# Create your views here.

def JobPostListView(request):
    jobs = JobPost.objects.all().order_by('-created_on')
    context = {
        'jobs' : jobs,
    }
    return render(request, "JobPost/list.html", context)

def JobPostDetailView(request, id):
    job = get_object_or_404(JobPost, id=id)
    context = {
        'job' : job,
    }
    return render(request, "JobPost/detail.html", context)

def JobPostSubmitView(request):
    if request.user.is_authenticated:
        form = JobPostForm()

        if request.method == "POST":
            form = JobPostForm(request.POST)

            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                creator = request.user
                created_on = datetime.now()
                url = form.cleaned_data['url']

                jobpost = JobPost(title=title, description=description, creator=creator, created_on=created_on, url=url)
                jobpost.save()
                return redirect('/')
        return render(request, 'JobPost/submit.html', {'form': form})
    return redirect('User/signin')

def JobPostEditView(request, id):
    post = get_object_or_404(JobPost, id=id)
    if (post.creator == request.user):
        if request.method == 'POST':
            form = JobPostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = JobPostForm(instance=post)
        return render(request, 'JobPost/submit.html', {'form': form})
    return redirect('/')

