import random
from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('golla_app:index')  # 수정된 부분
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    comments = article.comment_set.all()
    
    form = CommentForm()

    context = {
        'article': article,
        'form': form,
        'comments': comments,
    }

    return render(request, 'detail.html', context)


def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('golla_app:detail', id=id)  # 수정된 부분
        
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }

    return render(request, 'update.html', context)


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('golla_app:index')  # 수정된 부분


def comment_create(request, article_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            article = Article.objects.get(id=article_id)
            comment.article = article
            comment.save()

            return redirect('golla_app:detail', id=article_id)  # 수정된 부분

    else:
        return redirect('golla_app:index')  # 수정된 부분


def comment_delete(request, article_id, id):
    comment = Comment.get(id=id)
    comment.delete()

    return redirect('golla_app:detail', id=article_id)  # 수정된 부분

# 랜덤으로 게시물 보여주는 함수

def random_article(request):
    articles = Article.objects.all()
    if articles:
        article = random.choice(articles)
        context = {
            'article': article,
        }
        return render(request, 'random.html', context)
    else:
        return redirect('golla_app:index')