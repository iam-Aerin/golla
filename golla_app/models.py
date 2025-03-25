from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=255)
    choice_a = models.CharField(max_length=100)
    choice_b = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    selected = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B')])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
