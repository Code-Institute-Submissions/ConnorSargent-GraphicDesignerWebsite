from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .forms import PostForm
from .models import Post

# Create your views here.


def upcoming(request):
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }

    """ A view to return the upcoming page """
    return render(request, "upcoming/upcoming.html", context)


def add_post(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = PostForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.title = request.POST["title"]
                data.content = request.POST["content"]
                data.date_created = datetime.now()
                data.user = request.user
                data.save()
                messages.info(request, "Upcoming Post Added")
                return redirect("upcoming")
        else:
            form = PostForm()
        return render(request, "upcoming", {"form": form})


def delete_post(request, post_id):
    if request.user.is_superuser:
        post = Post.objects.get(id=post_id)

        if request.user == post.user:
            post.delete()

        return redirect("upcoming")


def edit_post(request, post_id):
    if request.user.is_superuser:
        post = Post.objects.get(id=post_id)

        if request.user.is_superuser:

            if request.method == "POST":
                form = PostForm(request.POST, instance=post)
                if form.is_valid():
                    data = form.save(commit=False)
                    data.save()
                    return redirect("upcoming")

            else:
                form = PostForm(instance=post)
                return render(request, "upcoming/edit_post.html",
                              {"form": form})
        else:
            return redirect("upcoming")
