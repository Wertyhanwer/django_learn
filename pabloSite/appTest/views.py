from django.urls import reverse

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Страница нашего тестового приложения")

def test(request, perem):
    return HttpResponse(f"Test<p>{perem}</p>")

def test2(request, int_perem):
    print("test2 отработал")
    if int_perem > 20000:
        print("вошли в инт")
        url = reverse('test3', args=[int_perem])
        print("reverse отработал")
        return redirect(url)
    return HttpResponse(f"{int_perem+5}")

def test3(request, int_perem):
    return HttpResponse(f"{int_perem+11}")

def test4(request):
    data = {'title': 'pablo'}
    return render(request, "appTest/index.html", data)

def page_not_found_custom(request, exception):
    return HttpResponseNotFound("ZV")