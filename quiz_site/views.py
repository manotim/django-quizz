from django.shortcuts import render
from .models import *


packages = [
    {
        'package_name': 'ATI TEAS 7 and HESI A2 Premium Package',
        'rate': 34,
        'days': 30,
        'services': {
            'service_1': 'TEAS 7 & HESI A2',
            'service_2': "Access to all subject's study guides. Well-detailed with an explanation",
            'service_3': 'Performance tracking',
            'service_4': 'Questions and well-detailed explanation',
            'service_5': 'Video explanation',
            'service_6': 'Detailed performance analysis available upon completion',
            'service_7': '1250 questions with 99% accuracy prediction of real exam',
            'service_8': '2 self-assessment practice 170 questions 309 minutes each'
        }
    },
    {
        'package_name': 'ATI TEAS 7 and HESI A2 Premium Plus Package',
         'rate': 189,
        'days': 80,
        'services': {
            'service_1': 'TEAS 7 & HESI A2',
            'service_2': "Access to all subject's study guides. Well-detailed with an explanation",
            'service_3': 'Performance tracking',
            'service_4': 'Questions and well-detailed explanation',
            'service_5': 'Video explanation',
            'service_6': 'Detailed performance analysis available upon completion',
            'service_7': '1250 questions with 99% accuracy prediction of real exam',
            'service_8': '2 self-assessment practice 170 questions 309 minutes each',
            'service_9': 'Live videos(maths & science)',
        }
    },
    {
        'package_name': 'Nursing Test Banks & EXIT EXAMS Package',
        'rate': 79,
        'days': 60,
        'services': {
            'service_1': 'HESI EXIT & ATI EXIT EXAMS',
            'service_2': "Comprehensive Nursing Curriculum",
            'service_3': 'Interactive Learning Modules',
            'service_4': 'Practice Quizzes and Exams',
            'service_5': 'Expert Faculty and Instructors',
            'service_6': 'Real-world Clinical Case Studies',
            'service_7': 'Collaborative Learning Communities',
            'service_8': 'Personalized Learning Paths',
            'service_9': '24/7 Access to Course Materials',
            'service_10': 'Continuing Education Resources',
        }
    }
]

# Create your views here.
def home(request):
    context = {
        'risks': Risk.objects.all(),
        'packages': Package.objects.all()
    }
    return render(request, 'quiz_site/home.html', context)

def about(request):
    return render(request, 'quiz_site/about.html')

def how_it_works(request):
    return render(request, 'quiz_site/how_it_works.html')


