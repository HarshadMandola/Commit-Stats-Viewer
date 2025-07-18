from django.shortcuts import render
from . models import Commits
from django.db.models import Sum,Count
from api.views import jira_view
# Create your views here.

def index(request):
    jira_view(request)
    commits=Commits.objects.all()
    total_commits=commits.count()
    total_merge=Commits.objects.filter(merge=True).count()
    total_added_lines = commits.aggregate(Sum('added_lines'))
    total_deleted_lines = commits.aggregate(Sum('deleted_lines'))
    total_added_lines_value = total_added_lines['added_lines__sum'] if total_added_lines['added_lines__sum'] is not None else 0
    total_deleted_lines_value = total_deleted_lines['deleted_lines__sum'] if total_deleted_lines['deleted_lines__sum'] is not None else 0
    overall_added_lines = total_added_lines_value - total_deleted_lines_value
    commits_per_day=Commits.objects.values('created_dates').annotate(commit_count=Count('hash_commit')).order_by('created_dates')
    dates=[]
    commit_count=[]
    for commit in commits_per_day:
        dates.append(commit['created_dates'])
        commit_count.append(commit['commit_count'])
    commits_per_author=Commits.objects.values('author_name').annotate(commit_count_per_person=Count('hash_commit')).order_by('author_name')
    author=[]
    author_commit=[]
    for iter in commits_per_author:
        author.append(iter['author_name'])
        author_commit.append(iter['commit_count_per_person'])

    context={
        "commits":commits,
        "total_commits":total_commits,
        "total_merge":total_merge,
        "overall_added_lines":overall_added_lines,
        "dates":dates,
        "commit_count":commit_count,
        "author":author,
        "author_commit":author_commit
    }
    return render(request,'harrychart/base2.html',context)