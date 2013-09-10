from django.core.management import setup_environ
import weevil.settings
setup_environ(weevil.settings)
from weevil.models import Magazine, Article, Contributor, Committee
from django.contrib.flatpages.models import FlatPage

import MySQLdb, getpass, re

Magazine.objects.all().delete()
Article.objects.all().delete()
Contributor.objects.all().delete()
Committee.objects.all().delete()
FlatPage.objects.all().delete()

cat = {
    44: 1,
    43: 2,
    42: 3,
    41: 4,
    39: 5,
    38: 6,
    49: 7,
    51: 8,
    52: 9,
    54: 10,
    55: 11,
    56: 12,
    57: 13
}

flat = {
    169: '/committee/getting-involved/', 
    272: '/committee/constitution/',
    # /committee/contact/
    177: '/supporters/',
    178: '/supporters/cusu-reprographics/'
}

committees = {
    168: 2013,
    392: 2012,
    274: 2011
}

def fixtext(text):
    return re.sub('"/?images/', '"http://www.weevilmagazine.co.uk/images/', text.decode('latin-1'))

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
    name = row[2].decode('latin-1')
    text = row[3].decode('latin-1')
    contributor = Contributor(name=name, slug=row[1], text=text)
    contributor.save()

c.execute('SELECT catid, alias, title, introtext, created_by_alias FROM jos_content WHERE sectionid=9 AND state=1')
# TODO Deal with multiple authors
created_re = re.compile('{ga=([^,&]*)(,?([^&,]*)&t)?}')
for row in c:
    if row[0] in cat:
        try:
            text = fixtext(row[3])
            title = row[2].decode('latin-1')
        except UnicodeDecodeError:
            print row[3]
            import sys
            sys.exit(0)
        article = Article(
            title=title,
            slug=row[1],
            text=text,
            magazine=weevils[cat[int(row[0])]]
        )
        m = created_re.match(row[4])
        if m:
            if m.group(1):
                article.author = Contributor.objects.get(slug=m.group(1))
            if m.group(3):
                article.illustrator = Contributor.objects.get(slug=m.group(3))
        article.save()
