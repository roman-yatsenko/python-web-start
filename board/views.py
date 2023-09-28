from django.http import HttpResponse

from .models import BoardMessage

def index(request):
    content = 'Список оголошень\n\n'
    for post in BoardMessage.objects.order_by('-published'):
        content += post.title + '\n' + post.content +'\n\n'
    return HttpResponse(content, content_type='text/plain; charset=utf-8')
    