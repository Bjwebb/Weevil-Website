from django.views.generic import DetailView, ListView, TemplateView
from weevil.models import Magazine, Article, Contributor, News, Committee
from django.db.models import Count 
from django.http import Http404

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self):
        return {
            'magazines': Magazine.objects.all(),
            'random_articles': Article.objects.order_by('?')[0:6],
            'recent_news': News.objects.all()[:3]
        }

class MagazineView(DetailView):
    def get_object(self):
        try:
            return Magazine.objects.get(
                issue_number=self.args[0]
            )
        except Magazine.DoesNotExist:
            raise Http404

class ArticleView(DetailView):
    def get_object(self):
        try:
            return Article.objects.get(
                magazine__issue_number=self.args[0],
                slug=self.args[1]
            )
        except Article.DoesNotExist:
            raise Http404

class SlugView(DetailView):
    def get_object(self):
        try:
            return self.model.objects.get(slug=self.args[0])
        except self.model.DoesNotExist:
            raise Http404

class ContributorsView(TemplateView):
    template_name = 'contributors.html'
    def get_context_data(self):
        c = {}
        if len(self.args) > 0:
            contype = self.args[0]
            if contype == 'writers':
                c[contype] = Contributor.objects.annotate(Count('articles_written')).filter(articles_written__count__gt=0)
            elif contype == 'illustrators':
                c[contype] = Contributor.objects.annotate(Count('articles_illustrated')).filter(articles_illustrated__count__gt=0)
        return c

class CommitteeView(DetailView):
    model = Committee
    def get_object(self):
        return self.model.objects.get(year=self.args[0])

home = HomeView.as_view()
magazine = MagazineView.as_view()
article = ArticleView.as_view()
contributors = ContributorsView.as_view()
contributor = SlugView.as_view(model=Contributor)
news = ListView.as_view(model=News)
#news_article = SlugView.as_view(model=News)
committee = CommitteeView.as_view()

