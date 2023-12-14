from django.shortcuts import render
from .models import *

# Create your views here.
def quizzes(request):
    context = {
        'questions': Question.objects.all(),
        'subjects': Subject.objects.all()
    }
    return render(request, 'quiz_bank/quizzes.html', context)

def math_quizzes_category(request):
    
    return render(request, 'quiz_bank/math/category_math.html')

def all_math_guides(request):
    
    return render(request, 'quiz_bank/math/guides/all_guides.html')

def abs_change_guide(request):
    
    return render(request, 'quiz_bank/math/guides/abs_change.html')

def language_study_guide(request):
    return render(request, 'quiz_bank/language_study_guide.html')