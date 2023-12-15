from django.shortcuts import render
from .models import *

# Create your views here.
def quizzes(request):
    
    return render(request, 'quiz_bank/quizzes.html')

def math_quizzes_category(request):
    
    return render(request, 'quiz_bank/math/category_math.html')

def all_math_guides(request):
    
    return render(request, 'quiz_bank/math/guides/all_guides.html')

def abs_change_guide(request):
    
    return render(request, 'quiz_bank/math/guides/abs_change.html')

def abs_change_practice(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'quiz_bank/math/guides/abs_change_prac.html', context)

def language_quizzes_category(request):
    return render(request, 'quiz_bank/language/category_language.html')

def all_language_guides(request):
    return render(request, 'quiz_bank/language/guides/all_guides.html')

def intro_to_teas_language(request):
    return render(request, 'quiz_bank/language/guides/intro_to_teas_lang.html')