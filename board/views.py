from django.shortcuts import render

from .models import BoardMessage

def index(request):
    posts = BoardMessage.objects.order_by('-published')
    context = {'posts': posts}
    return render(request, 'board/index.html', context)
            