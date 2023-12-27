from django.urls import path
from .views import (
    QuestionListView, 
    # QuestionDetailView, 
    QuestionCreateView
)
from . import views

urlpatterns = [
    path('', views.quizzes, name='quizzes-home'),

    # MATH HERE
    path('category/math/', views.math_quizzes_category, name='math-quizzes-category'),
    path('category/math/guides', views.all_math_guides, name='all-math-guides'),
    # math guides here
    path('category/math/guides/abs-change', views.abs_change_guide, name='abs-change-guide'),
    path('category/math/guides/abs-change-prac', QuestionListView.as_view(), name="abs-change-practice"),
    # path('category/math/guides/abs-change-prac/quiz/<int:pk>', QuestionDetailView.as_view(), name="abs-change-practice-detail"),
    path('category/math/guides/abs-change-prac/quiz/new/', QuestionCreateView.as_view(), name="abs-change-practice-create"),

    path('category/math/guides/money-management/', views.money_management_guide, name='money-management-guide'),

    path('category/math/guides/proportions/', views.proportions_guide, name='proportions-guide'),

    path('category/math/guides/variables_&_eqs/', views.variables_and_eqs_guide, name='vars-eqs-guide'),

    path('category/math/guides/dep_&_indep_vars/', views.dependent_and_independent_variables, name='dep-and-indep-vars-guide'),

    path('category/math/guides/visualizing_data/', views.visualizing_data, name='visualizing-data-guide'),

    # LANGUAGE HERE
    path('category/language/', views.language_quizzes_category, name="language-quizzes-category"),
    path('category/language/guides', views.all_language_guides, name='all-language-guides'),
    # language guides here
    path('category/language/guides/intro-to-teas-lang', views.intro_to_teas_language, name='intro-to-teas-lang-guide'),
    path('category/language/guides/academic-thesis', views.academic_thesis_guide, name='academic-thesis-guide'),
    path('category/language/guides/simple&compound-sentences', views.compound_and_simple_sentences_guide, name='simple-compound-guide'),
    path('category/language/guides/coherence_writing', views.coherence_in_writing_guide, name='coherence-writing-guide'),
    path('category/language/guides/dangling_modifiers', views.dangling_modifiers_guide, name='dangling-modifiers-guide'),
    path('category/language/guides/parts-of-speech', views.parts_of_speech_guide, name='parts-of-speech-guide'),

    # READING HERE
    path('category/reading/', views.reading_quizzes_category, name="reading-quizzes-category"),
    path('category/reading/guides', views.all_reading_guides, name='all-reading-guides'),
    # reading guides here
    path('category/reading/guides/topic-main-ideas', views.topic_main_idea_supporting_details, name='topic-main-guide'),
    path('category/reading/guides/summarizing-reading-guide', views.summarizing_reading_guide, name='summarizing-reading-guide'),
    path('category/reading/guides/sequence-of-events', views.seq_of_events_guide, name='sequency-of-events-guide'),
    path('category/reading/guides/info-in-text', views.finding_info_in_text, name='info-in-text-guide'),
    path('category/reading/guides/inconsistencies-in-text', views.inconsistencies_in_text, name='inconsistencies-in-text-guide'),
    path('category/reading/guides/predictions-on-info', views.predictions_on_information_guide, name='predictions-on-info-guide'),

    # READING HERE
    path('category/science/', views.science_quizzes_category, name="science-quizzes-category"),
    path('category/science/guides', views.all_science_guides, name='all-science-guides'),
]