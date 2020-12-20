from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hi_maxim(request):
    return HttpResponse('Zdraste')

def task(request):
    return HttpResponse('django rulezz')