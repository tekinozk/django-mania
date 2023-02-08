from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from blog.models import BlogCategory,BlogTag,Post

def all_post_view(request):
    categories = BlogCategory.objects.filter(is_active=True).order_by("title")
    tags = BlogTag.objects.filter(is_active=True).order_by("title")
    posts = Post.objects.filter(is_active=True).order_by("-created_at")
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context=dict(
        categories=categories,
        tags=tags,
        posts=posts,
        page_obj=page_obj,
       
    )
    return render(request,"blog/all_posts.html",context)

def category_view(request,category_slug):
    category =get_object_or_404(BlogCategory,slug=category_slug)
    categories = BlogCategory.objects.filter(is_active=True).order_by("title")
    tags = BlogTag.objects.filter(is_active=True).order_by("title")
    posts = Post.objects.filter(is_active=True,category=category).order_by("-created_at")
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context=dict(
        categories=categories,
        tags=tags,
        posts=posts,
        category=category,
        page_obj=page_obj,
    )
    return render(request,"blog/all_posts.html",context)

def tag_view(request,tag_slug):
    tag =get_object_or_404(BlogTag,slug=tag_slug)
    categories = BlogCategory.objects.filter(is_active=True).order_by("title")
    tags = BlogTag.objects.filter(is_active=True).order_by("title")
    posts = Post.objects.filter(is_active=True,tag=tag).order_by("-created_at")
    context=dict(
        categories=categories,
        tags=tags,
        posts=posts,
        tag=tag
    )
    return render(request,"blog/all_posts.html",context)

def post_detail(request,post_slug,category_slug):
    post = get_object_or_404(Post,slug=post_slug)
    categories = BlogCategory.objects.filter(is_active=True).order_by("title")
    tags = BlogTag.objects.filter(is_active=True).order_by("title")
    post.view_count = post.view_count + 1
    post.save()
    context=dict(
        categories=categories,
        tags=tags,
        post=post,
       
    )
    return render(request,"blog/post_detail.html",context)