from django.db import models
from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey

class Magazine(Sortable):
    class Meta:
        ordering = ['issue_number']

    issue_number = models.IntegerField()
    text = models.TextField(default='')
    cover = models.ImageField(upload_to='cover', null=True)
    
    published = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return 'Weevil #'+str(self.issue_number)

class Contributor(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    text = models.TextField(default='')

    legacy_is_illustractor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Article(Sortable):
    class Meta(Sortable.Meta):
        pass
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=100)
    text = models.TextField(default='')
    author = models.ForeignKey(Contributor, related_name='articles_written', null=True, blank=True)
    illustrator = models.ForeignKey(Contributor, related_name='articles_illustrated', null=True, blank=True)
    legacy_id = models.IntegerField(null=True, editable=False)
    
    magazine = SortableForeignKey(Magazine)

    def __unicode__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=100)
    text = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Committee(models.Model):
    year = models.IntegerField()
    text = models.TextField(default='')

    def __unicode__(self):
        return unicode(self.year)


