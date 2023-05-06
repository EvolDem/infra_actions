from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось задеплоить это в облако!!!1адин')


def second_page(request):
    return HttpResponse('А это вторая страница!')
