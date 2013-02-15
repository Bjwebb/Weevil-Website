from django.db import models

class Magazine(models.Model):
    issue_number = models.IntegerField()
    text = models.TextField(default='')
    
    published = models.DateTimeField()

    def __unicode__(self):
        return 'Weevil #'+str(self.issue_number)


class Article(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField()
    text = models.TextField(default='')
    author = models.ForeignKey(Contributor)
    illustrator = models.ForeignKey(Contributor)
    
    magazine = models.ForeignKey(Magazine)

    def __unicode__(self):
        return self.title

class Contributor(models.Model):
    name = models.CharField()
    slug = models.SlugField()
    text = models.TextField(default='')
