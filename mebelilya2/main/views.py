from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review

def home(request):
    return render(request, 'home.html')

def catalog(request):
    products = [
        {
            'name': 'Угловой диван "Комфорт"',
            'price': '120 000 ₸',
            'material': 'велюр',
            'photo': 'main/sofa.jpg'
        },
        {
            'name': 'Кресло "Релакс"',
            'price': '65 000 ₸',
            'material': 'эко-кожа',
            'photo': 'main/armchair.jpg'
        },
        {
            'name': 'Обеденный стол "Семейный"',
            'price': '89 000 ₸',
            'material': 'массив дерева',
            'photo': 'main/table.jpg'
        },
        {
            'name': 'Шкаф-купе "Престиж"',
            'price': '150 000 ₸',
            'material': 'ЛДСП',
            'photo': 'main/wardrobe.jpg'
        },
    ]
    return render(request, 'catalog.html', {'products': products})


def gallery(request):
    photos = [
        {'src': 'main/gallery1.jpg', 'review': 'Очень доволен покупкой!'},
        {'src': 'main/gallery2.jpg', 'review': 'Мебель качественная и красивая.'},
        {'src': 'main/gallery3.jpg', 'review': 'Прекрасный сервис и быстрая доставка!'},
        {'src': 'main/gallery4.jpg', 'review': 'Спасибо за уют в моем доме!'},
        {'src': 'main/gallery5.jpg', 'review': 'Всё соответствует описанию.'},
        {'src': 'main/gallery6.jpg', 'review': 'Буду заказывать ещё.'},
        {'src': 'main/gallery7.jpg', 'review': 'Очень красиво смотрится в интерьере.'},
    ]

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ReviewForm()

    reviews = Review.objects.order_by('-date')[:5]
    return render(request, 'gallery.html', {
        'photos': photos,
        'form': form,
        'reviews': reviews
    })

def about(request):
    owner_info = {
        'name': 'Илья Домашников',
        'bio': 'Основатель "Домашнего уюта", дизайнер интерьеров с 15-летним опытом. Любовь к уюту и теплу вдохновила на создание собственного мебельного магазина.',
        'file': 'owner_info.pdf'
    }
    return render(request, 'about.html', {'owner': owner_info})

def contacts(request):
    return render(request, 'contacts.html')

def feedback(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = ReviewForm()
    reviews = Review.objects.order_by('-date')[:5]  # показываем 5 последних
    return render(request, 'feedback.html', {'form': form, 'reviews': reviews})