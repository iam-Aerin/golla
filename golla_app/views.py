from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from random import choice

def index(request):
    questions = Question.objects.order_by('-created_at')  # 최신순 정렬
    return render(request, 'golla_app/index.html', {
        'questions': questions
    })


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('golla_app:index')
    else:
        form = QuestionForm()
    return render(request, 'golla_app/create.html', {'form': form})

def detail(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answers.all()
    form = AnswerForm()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('golla_app:detail', id=question.id)

    a_count = answers.filter(selected='A').count()
    b_count = answers.filter(selected='B').count()
    total = answers.count()
    a_percent = round((a_count / total) * 100, 1) if total else 0
    b_percent = round((b_count / total) * 100, 1) if total else 0

    context = {
        'question': question,
        'form': form,
        'answers': answers,
        'a_percent': a_percent,
        'b_percent': b_percent,
    }
    return render(request, 'golla_app/detail.html', context)

def edit_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('golla_app:detail', id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'golla_app/edit_answer.html', {'form': form, 'answer': answer})

def random_article(request):
    questions = Question.objects.all()
    if questions.exists():
        question = choice(questions)
        return redirect('golla_app:detail', id=question.id)
    return redirect('golla_app:index')
