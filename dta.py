from django.http import HttpResponse
from django.template import loader

from .models import Article


def index(request):
    article = Article()
    article.title = 'This is the title'
    article.contents = 'This is the content'
    article.save()

    template = loader.get_template('articles/index.html')
    context = {
        'new_article_id': article.pk,
    }
    return HttpResponse(template.render(context, request))