from django.shortcuts import render, redirect
from .forms import *
from .models import Review

# Create your views here.

def index(request):
    reviews = Review.objects.all()

    context = {
        "reviews": reviews,
    }
    """ Index page view """
    return render(request, 'home/index.html', context)


def add_review(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.save()
                return redirect("home")
        else:
            form = ReviewForm()
        return render(request, 'home/index.html', {"form": form})
