from django.shortcuts import render, redirect
from .forms import ReviewForm
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
                messages.info(request, 'Testamonial Added')
        else:
            form = ReviewForm()
        return render(request, 'home', {"form": form})


def delete_review(request, review_id):
    if request.user.is_authenticated:
        review = Review.objects.get(id=review_id)

        if request.user == review.user:
            review.delete()
            messages.info(request, 'Testamonial Deleted')

        return redirect("home")


def edit_review(request, review_id):
    if request.user.is_authenticated:
        review = Review.objects.get(id=review_id)

        if request.user == review.user:

            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 5) or (data.rating < 0):
                        error = "Out or range. Please select rating from 0 to 5."
                        return render(request, 'home/edit_review.html', {"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("home")
                        messages.info(request, 'Testamonial Edited')
            else:
                form = ReviewForm(instance=review)
                return render(request, 'home/edit_review.html', {"form": form})
        else:
            return redirect("home")
