from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogPost,Comment
from .forms import BlogPostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
# List all blog posts with search and pagination
def post_list(request):
    query=request.GET.get('q','')
    if query:
        posts=BlogPost.objects.filter(Q(title_icontains=query)) | (Q(content_icontains=query))
    else:
        posts=BlogPost.objects.all()
    paginator=Paginator(posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page('page_number')
    return render(request,'blogapp/post_list.html',{'page_obj':page_obj,'query':query})
# View a single blog post with comments
def post_detail(request,pk):
    post=get_object_or_404(BlogPost,pk=pk)
    comment=comment.all()
    if request.method=="POST":
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.author=request.user
            comment.post=post
            comment.save()
            return redirect('post_details',pk=post.pk)
    else:
        comment_form=CommentForm()
    return render(request,'blogapp/post_detail.html',{'post':post,'comment':comment,'comment_form':comment_form})

# Create a new blog post
@login_required
def post_create(request):
    if request.method=="POST":
        form=BlogPostForm(request.POST)
        if form.is_valid():
           post=form.save(commit=False)
           post.author=request.user
           post.save()
           form.save_m2m() # Save many-to-many relationship for tags
           return redirect ('post_list')
    else:
        form=BlogPostForm()
    return render(request,'blogapp/post_form.html',{'form':form})

# Edit an existing blog post
@login_required 
def post_edit(request,pk):
    post=get_object_or_404(BlogPost,pk=pk)
    if request.method=="POST":
        form=BlogPostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            form.save_m2m()# Save many-to-many relationship for tags
            return redirect('post_detail',pk=post.pk)
    else:
        form=BlogPostForm(instanse=post) 
        return render(request,"blogapp/post_from.html",{'form':form}) 
