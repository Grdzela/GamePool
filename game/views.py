from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
import json

menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "About", 'url_name': 'about'},
        {'title': "Games", 'url_name': 'games'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Login", 'url_name': 'login'},
        ]


def game(request):
    games = Product.objects.all()
    cats = Category.objects.all()

    context = {
        'games': games,
        'cats': cats,
        'title': 'GamePool',
        'cat_selected': 0,
    }
    return render(request, 'game/main.html', context=context)


def layout(request):
    return render(request, 'game/layout.html',)


def about(request):
    return render(request, 'game/about.html', {'menu': menu, 'title': 'About'})


def contact(request):
    return render(request, 'game/contact.html')


def detail_page(request, id):
    prods = get_object_or_404(Product, pk=id)
    return render(request, 'game/detail.html', {'prods': prods})


# def show_post(request, post_id, Product):
#     prods = Product.objects.all()
#     return render(request, 'game/detail.html', {'prods': prods}, {post_id})

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An arror occured during registration')
    return render(request, 'game/register.html', {'form': form})


def login(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('game')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User dose not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('game')
        else:
            messages.error(request, 'Username OR password dose not exist')

    context = {'page': page}
    return render(request, 'game/login.html', context)


@csrf_exempt
# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('Action:', action)
#     print('Product:', productId)
#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     return JsonResponse('Item was added', safe=False)
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_category(request, cat_id):
    games = Product.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    # if len(posts) == 0:
    #     raise Http404()

    context = {
        'games': games,
        'cats': cats,
        'menu': menu,
        'title': 'Show Category',
        'cat_selected': cat_id,
    }

    return render(request, 'game/main.html', context=context)
