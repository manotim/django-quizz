from django.shortcuts import render

questions = [
    {
        'question_text': 'What is the name of Man U coach?',
        'option_a': 'Ole Guna',
        'option_b': 'Jose Mou',
        'option_c': 'Alex Fergie',
        'option_d': 'Jurgen Klop',
        'correct_answer': 'C',
        'explanation': 'Fergie is the real OG for the Red Devils! The rest are just wicked crooks!'
    },
    {
        'question_text': 'When is Christmas?',
        'option_a': '20th Oct',
        'option_b': '25th Dec',
        'option_c': '14th Feb',
        'option_d': '1st Jan',
        'correct_answer': 'B',
        'explanation': 'Some clever fools in the ancient times decided for the world ass population that Jesus was born on  25th Dec. Something not mentioned anywhere in any spiritual book. Ridiculous!'
    },
]

# Create your views here.
def quizzes(request):
    context = {
        'questions': questions
    }
    return render(request, 'quiz_bank/quizzes.html', context)