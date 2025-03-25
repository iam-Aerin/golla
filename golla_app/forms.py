from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'choice_a', 'choice_b']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '질문을 입력하세요.'}),
            'choice_a': forms.TextInput(attrs={'placeholder': '보기 A를 입력하세요.'}),
            'choice_b': forms.TextInput(attrs={'placeholder': '보기 B를 입력하세요.'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['selected', 'comment']
        widgets = {
            'selected': forms.TextInput(attrs={'placeholder': 'A 또는 B'}),
            'comment': forms.Textarea(attrs={'placeholder': '내용을 입력하세요.'}),
        }
