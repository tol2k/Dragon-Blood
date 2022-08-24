from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some','Hello']
    }
    return  render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': 'О нас',

    }
    return render(request, 'main/about.html',data)

def father(request):
    data = {
        'title': 'Отец',

    }
    return render(request, 'main/father.html', data)