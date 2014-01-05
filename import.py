import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'weevil.settings'
from weevil.models import Magazine, Article, Contributor, Committee
from django.contrib.flatpages.models import FlatPage

import MySQLdb, getpass, re

Magazine.objects.all().delete()
Article.objects.all().delete()
Contributor.objects.all().delete()
Committee.objects.all().delete()
FlatPage.objects.all().delete()

from weevil.legacy import category_mapping as cat
from weevil.legacy import flat_mapping as flat
from weevil.legacy import committee_mapping as committees


def fixtext(text):
    return re.sub('"/?images/', '"http://www.weevilmagazine.co.uk/images/', text.decode('utf-8'))

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd=getpass.getpass(), db='weevil') 
c = conn.cursor()

for id_, year in committees.items():
    c.execute('SELECT introtext FROM jos_content WHERE id={0}'.format(id_))
    for row in c:
        committee = Committee(year=year)
        committee.text = fixtext(row[0])
        committee.save()

for id_, url in flat.items():
    c.execute('SELECT introtext FROM jos_content WHERE id={0}'.format(id_))
    for row in c:
        flatpage = FlatPage(url=url)
        flatpage.content = fixtext(row[0])
        flatpage.save()
        flatpage.sites.add(1)

weevils = {}
c.execute('SELECT id,description FROM jos_categories WHERE section=9;')
for row in c:
    if row[0] in cat:
        i = cat[row[0]]
        weevil = Magazine(issue_number=i)
        weevil.text = fixtext(row[1])
        weevils[i] = weevil
        weevil.save()

c.execute('SELECT catid, alias, title, introtext FROM jos_content WHERE sectionid=6 AND state=1')
for row in c:
    name = row[2].decode('utf-8')
    text = row[3].decode('utf-8')
    contributor = Contributor(name=name, slug=row[1], text=text)
    if row[0] == 40:
        contributor.legacy_is_illustractor = True
    contributor.save()

c.execute('SELECT catid, alias, title, introtext, created_by_alias, id, ordering FROM jos_content WHERE sectionid=9 AND state=1 ORDER BY ordering')
# TODO Deal with multiple authors
created_re = re.compile('{ga=([^}&]*)')
for row in c:
    if row[0] in cat:
        try:
            text = fixtext(row[3])
            title = row[2].decode('utf-8')
        except UnicodeDecodeError:
            print row[3]
            import sys
            sys.exit(0)
        article = Article(
            title=title,
            slug=row[1],
            text=text,
            magazine=weevils[cat[int(row[0])]],
            legacy_id=row[5]
        )
        m = created_re.match(row[4])
        if m:
            for slug in m.group(1).split(','):
                contributor = Contributor.objects.get(slug=slug)
                if contributor.legacy_is_illustractor:
                    article.illustrator = contributor
                else:
                    article.author = contributor
            article.save()
