from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'choice_a', 'choice_b']
        labels = {
            'title': '🖥️문제줘🤖',
            'choice_a': '🅰️',
            'choice_b': '🅱️',
        } 
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '질문을 입력하세요.'}),
            'choice_a': forms.TextInput(attrs={'placeholder': '보기 A를 입력하세요.'}),
            'choice_b': forms.TextInput(attrs={'placeholder': '보기 B를 입력하세요.'}),
        }

class AnswerForm(forms.ModelForm):
    selected = forms.ChoiceField(
        choices=[('A', 'A'), ('B', 'B')],
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,  # 필수 선택
        label='답변:'
    )

    class Meta:
        model = Answer
        fields = ['selected', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': '내용을 입력하세요.',
                'class': 'form-control',
                'rows': 4,
                'required': True,  # 필수 입력
            }),
        }