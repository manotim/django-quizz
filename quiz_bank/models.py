from django.db import models
from django.urls import reverse

class Question(models.Model):
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)
    explanation = models.TextField()

    def __str__(self):
        return self.question_text
    
    # def get_absolute_url(self):
    #     return reverse("abs-change-practice-detail", kwargs={"pk": self.pk})
    
    

