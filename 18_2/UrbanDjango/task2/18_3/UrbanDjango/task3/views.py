from django.shortcuts import render

# Create your views here.
def platform(request):
    context = {
        'title': 'platform'
    }
    return render(request, 'third_task/platform.html', context)

def games(request):
    context = {
        'title': 'games',
        'game_list': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']
    }
    return render(request, 'third_task/games.html', context)

def cart(request):
    context = {
        'title': 'cart'
    }
    return render(request, 'third_task/cart.html', context)