from django.views.generic import DetailView, ListView, TemplateView
from weevil.models import Magazine, Article, Contributor

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self):
        return {
            'magazines': Magazine.objects.all(),
            'random_articles': Article.objects.order_by('?')[0:6],
        }

class MagazineView(DetailView):
    def get_object(self):
        return Magazine.objects.get(
            issue_number=self.args[0]
        )

class ArticleView(DetailView):
    def get_object(self):
        return Article.objects.get(
            magazine__issue_number=self.args[0],
            slug=self.args[1]
        )

class SlugView(DetailView):
    def get_object(self):
        return self.model.objects.get(slug=self.args[0])

home = HomeView.as_view()
magazine = MagazineView.as_view()
article = ArticleView.as_view()
contributor = SlugView.as_view(model=Contributor)

