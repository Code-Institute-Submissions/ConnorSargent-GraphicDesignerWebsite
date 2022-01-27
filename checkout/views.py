from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KMac3CoXNGJfnT786PzbxvtXW2jYP5XXWtj5JOhuMgIlM6pF8Kx2rCYx8fPVCV6LyQBTnzB5Y8HDAbW79E6S1rV00LCRZNjr3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
