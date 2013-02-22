from django.db import models

class Magazine(models.Model):
    issue_number = models.IntegerField()
    text = models.TextField(default='')
    
    published = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return 'Weevil #'+str(self.issue_number)

class Contributor(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    text = models.TextField(default='')

    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=100)
    text = models.TextField(default='')
    author = models.ForeignKey(Contributor, related_name='articles_written', null=True, blank=True)
    illustrator = models.ForeignKey(Contributor, related_name='articles_illustrated', null=True, blank=True)
    
    magazine = models.ForeignKey(Magazine)

    def __unicode__(self):
        return self.title

