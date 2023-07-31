from django.urls import path
from . import views
from . import technical_error

from django.urls import path
from .views import *
from .conditional_number import  *

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name='update'),
    path('search/', views.search, name='search'),
    path('technical_error', technical_error.homeTE, name='technical_error'),
    path('technical_detail/<int:id>', technical_error.detailTE, name='technical_detail'),
    path('technical_error_create/', technical_error.createTE, name='technical_error_create'),
    path('technical_error_update/<int:id>', technical_error.updateTE, name='technical_error_update'),
    path('exportcsv', views.exportcsv, name='exportcsv'),
    path('exportcsvTE', technical_error.exportcsvTE, name='exportcsvTE'),

]