from django.shortcuts import render

from .models import BoardMessage, Rubric

def index(request):
    posts = BoardMessage.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'posts': posts,
        'rubrics': rubrics,
    }
    return render(request, 'board/index.html', context)


def by_rubric(request, rubric_id):
    posts = BoardMessage.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)        
    # context = {
    #     'post': posts,
    #     'rubrics': rubrics,
    #     'current_rubrics': current_rubric,
    # }
    # return render(request, 'board/by_rubric.html', context)
    return render(request, 'board/by_rubric.html', locals())
