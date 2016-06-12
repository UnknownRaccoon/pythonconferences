from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from django.views import generic


class ArticlesView(LoginRequiredMixin, generic.ListView):
    paginate_by = 5
    model = Article
    template_name = 'articles/index.html'


class ArticleView(LoginRequiredMixin, generic.DetailView):
    model = Article
    template_name = 'articles/article.html'
