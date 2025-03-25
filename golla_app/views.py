from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def question_list(request):
    questions = Question.objects.order_by('-created_at')
    return render(request, 'golla_app/question_list.html', {'questions': questions})

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question-list')
    else:
        form = QuestionForm()
    return render(request, 'golla_app/question_create.html', {'form': form})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    form = AnswerForm()

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('question-detail', pk=pk)

    # 통계 계산
    total = answers.count()
    a_count = answers.filter(selected='A').count()
    b_count = answers.filter(selected='B').count()
    a_percent = round((a_count / total) * 100, 2) if total else 0
    b_percent = round((b_count / total) * 100, 2) if total else 0

    context = {
        'question': question,
        'answers': answers,
        'form': form,
        'a_percent': a_percent,
        'b_percent': b_percent,
    }
    return render(request, 'golla_app/question_detail.html', context)
