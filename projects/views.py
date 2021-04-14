from django.shortcuts import render, HttpResponse, redirect
from projects.models import Project
from django.contrib import messages

# Create your views here.


#APIs
def projecthome(request):
    allprojects = Project.objects.all()
    context = {'allprojects': allprojects}
    return render(request, 'project/projecthome.html', context)
    #return HttpResponse('This is bloghome. We will keep all the blogs here.')
   

def projectPost(request, slug):
    project = Project.objects.filter(slug=slug).first()
    #comments = projectComment.objects.filter(post=post)
    context = {'project':project}
    return render(request, 'project/projectPost.html', context)
    #return HttpResponse(f'This is Blog: {slug}')

def projectsearch(request):
    queries = request.GET['queries']
    if len(queries)>78:
        allprojects= []
    else:
        allprojects = Project.objects.filter(title__icontains = queries)
    params = {'allprojects':allprojects, 'queries':queries}
    return render(request, 'project/projectsearch.html', params)
   
 
