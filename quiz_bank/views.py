from django.shortcuts import render
from .models import *

# Create your views here.
def quizzes(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'quiz_bank/quizzes.html', context)