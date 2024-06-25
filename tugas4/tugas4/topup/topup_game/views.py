from django.shortcuts import render, redirect
from .forms import TopUpForm
from .models import Transaction


def home(request):
    return render(request, 'home.html')

def top_up(request, game_name):
    top_up = [
        {
            'title': 'Weekly Diamond Pass',
            'description': 'Get 100 diamonds every week.',
            'price': 'Rp8.700',
            'bonus': 'No Bonus'
        },
        {
            'title': '28 Diamonds',
            'description': '25 + 3 Bonus',
            'price': 'Rp8.900',
            'bonus': '3 Diamonds'
        },
        {
            'title': '59 Diamonds',
            'description': '50 + 9 Bonus',
            'price': 'Rp8.500',
            'bonus': '9 Diamonds'
        },
    
    ]

    return render(request, 'topup.html', {'top_up': top_up})

def success(request):
    return render(request, 'success.html')

