from django.shortcuts import render

# Create your views here.

def upcoming(request):
    """ A view to return the upcoming page """

    return render(request, 'upcoming/upcoming.html')