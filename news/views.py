from .models import Article
from django.views import generic


class ArticlesView(generic.ListView):
    paginate_by = 5
    model = Article
    template_name = 'articles/index.html'


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'articles/article.html'
