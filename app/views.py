from django.shortcuts import render  # Импорт функции render для рендеринга шаблонов
from django.http import HttpResponse  # Импорт класса HttpResponse для создания HTTP-ответов
from django.views.decorators.csrf import csrf_exempt  # Импорт декоратора csrf_exempt для отключения CSRF-защиты

def index(request):  # Определение представления index
    selected_genre = request.COOKIES.get('selected_genre', 'Не выбран') # Получение значения выбранного жанра из куки, если нет куки — 'Не выбран'
    selected_theme = request.COOKIES.get('selected_theme', 'light')  # Получение значения выбранной темы из куки, если нет куки — 'light'
    context = {  # Создание контекста для передачи в шаблон
        'selected_genre': selected_genre,  
        'selected_theme': selected_theme,  
    }
    return render(request, 'app/index.html', context)  # Рендеринг шаблона index.html с переданным контекстом

@csrf_exempt  # Отключение CSRF-защиты для этого представления
def select_genre(request):  # Определение представления select_genre
    if request.method == 'POST':  # Проверка, является ли метод запроса POST
        genre = request.POST.get('genre')  # Получение значения жанра из POST-данных
        response = HttpResponse("Вы выбрали жанр: " + genre)  # Создание HTTP-ответа с сообщением о выбранном жанре
        response.set_cookie('selected_genre', genre)  # Установка куки с выбранным жанром
        return response  # Возврат HTTP-ответа
    return HttpResponse("Метод не поддерживается")  # Возврат HTTP-ответа с сообщением об ошибке, если метод запроса не POST

@csrf_exempt  
def select_theme(request):  
    if request.method == 'POST': 
        theme = request.POST.get('theme') 
        response = HttpResponse("Вы выбрали тему: " + theme)  
        response.set_cookie('selected_theme', theme)  
        return response 
    return HttpResponse("Метод не поддерживается") 
