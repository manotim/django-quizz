from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizzes, name='quizzes-home'),

    # MATH HERE
    path('category/math/', views.math_quizzes_category, name='math-quizzes-category'),
    path('category/math/guides', views.all_math_guides, name='all-math-guides'),
    # math guides here
    path('category/math/guides/abs-change', views.abs_change_guide, name='abs-change-guide'),
    path('category/math/guides/abs-change-prac', views.abs_change_practice, name="abs-change-practice"),

    # LANGUAGE HERE
    path('category/language/', views.language_quizzes_category, name="language-quizzes-category"),
    path('category/language/guides', views.all_language_guides, name='all-language-guides'),
    # language guides here
    path('category/language/guides/intro-to-teas-lang', views.intro_to_teas_language, name='intro-to-teas-lang-guide'),
]