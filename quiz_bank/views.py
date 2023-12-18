from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
    )
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

def money_management_guide(request):
    return render(request, 'quiz_bank/math/guides/money_mngnt.html')

def proportions_guide(request):
    return render(request, 'quiz_bank/math/guides/proportions.html')

def variables_and_eqs_guide(request):
    return render(request, 'quiz_bank/math/guides/vars_&_eqs.html')

def variables_and_eqs_guide(request):
    return render(request, 'quiz_bank/math/guides/vars_&_eqs.html')

def dependent_and_independent_variables(request):
    return render(request, 'quiz_bank/math/guides/dep_&_indep_vars.html')

def visualizing_data(request):
    return render(request, 'quiz_bank/math/guides/visualizing_data.html')

def abs_change_practice(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'quiz_bank/math/guides/abs_change_prac.html', context)

class QuestionListView(ListView):
    model = Question
    template_name = 'quiz_bank/math/guides/abs_change_prac.html'
    context_object_name = 'questions'
    paginate_by = 1

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(CreateView):
    model = Question
    fields = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'explanation']



def language_quizzes_category(request):
    return render(request, 'quiz_bank/language/category_language.html')

def all_language_guides(request):
    return render(request, 'quiz_bank/language/guides/all_guides.html')

def intro_to_teas_language(request):
    return render(request, 'quiz_bank/language/guides/intro_to_teas_lang.html')