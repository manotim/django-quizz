from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('about/', views.about, name='quiz-about'),
    path('how-it-works/', views.how_it_works, name='how-it-works')
]
