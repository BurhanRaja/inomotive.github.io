from django.shortcuts import render, HttpResponse, redirect
from blogs.models import Post, BlogComment
from django.contrib import messages
import time

# Create your views here.


#APIs
def bloghome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog/bloghome.html', context)
    #return HttpResponse('This is bloghome. We will keep all the blogs here.')
   

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post)
    context = {'post':post, 'comments':comments, 'user':request.user}
    print(request.user)
    return render(request, 'blog/blogPost.html', context)
    #return HttpResponse(f'This is Blog: {slug}')

def search(request):
    #allPosts = Post.objects.all()
    query = request.GET['query']
    if len(query)>78:
        allPosts= []
    else:
        allPosts = Post.objects.filter(title__icontains = query)
    params = {'allPosts':allPosts, 'query':query}
    return render(request, 'blog/search.html', params)
   
 
def postComment(request):
    if request.method == 'POST':
            comment = request.POST.get("comment") 
            user = request.user
            postsno = request.POST.get("postsno")
            post = Post.objects.get(sno=postsno)


            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted Successfully")
    return redirect(f"/blogs/{post.slug}")
    #return render(request, 'blog/blogPost.html', context)
    #return HttpResponse(f'This is Blog: {slug}')
         
      
   
    
   