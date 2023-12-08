from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer', 'explanation']
