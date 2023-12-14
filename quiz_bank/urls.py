from django.urls import path
from . import views

urlpatterns = [
    path('', views.quizzes, name='quizzes-home'),
    path('category/math/', views.math_quizzes_category, name='math-quizzes-category'),
    path('category/math/guides', views.all_math_guides, name='all-math-guides'),
    path('category/math/guides/abs-change', views.abs_change_guide, name='abs-change-guide'),
    path('category-guides/study_guide_language/', views.language_study_guide, name='language-study-guide'),
]