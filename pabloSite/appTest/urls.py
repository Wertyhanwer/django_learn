from django.urls import path, register_converter
from django.views.defaults import page_not_found

from . import views, convertors

register_converter(convertors.ABConvertor, "PabloMamba")

urlpatterns = [
    path('test/<int:perem>/', views.test),
    path("test2/<PabloMamba:int_perem>/",views.test2, name='test2'),
    path("test3/<PabloMamba:int_perem>/",views.test3, name='test3'),
    path("test4/",views.test4, name='test4')
]
