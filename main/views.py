from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404

from main.forms import CreatePostForm, RegisterForm, CreateCommentForm
from main.models import Post, Comment


def list_posts_view(request):
    posts = Post.objects.all()
    return render(request, "list_post.html", {
        "posts": posts
    })


@login_required
def create_post_view(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(f"/posts/{post.id}/")
    else:
        form = CreatePostForm(initial={
            "author": request.user
        })
    return render(request, "create_post.html", {
        "form": form
    })


def get_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by("-created_at")
    return render(
        request, "view_post.html",
        {
            "post": post,
            "comments": comments,
            "form": CreateCommentForm()
        }
    )


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["login"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def home_view(request):
    return redirect("/posts/")


@login_required
def create_comment_view(request, post_id):
    if request.method == "POST":
        form = CreateCommentForm(request.POST)
        post = get_object_or_404(Post, id=post_id)
        if form.is_valid():
            Comment.objects.create(
                author=request.user,
                post=post,
                text=form.cleaned_data["text"]
            )
    return redirect(f"/posts/{post_id}")
