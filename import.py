from django.core.management import setup_environ
import weevil.settings
setup_environ(weevil.settings)
from weevil.models import Magazine, Article, Contributor

import MySQLdb, getpass, re

Magazine.objects.all().delete()
Article.objects.all().delete()
Contributor.objects.all().delete()

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

weevils = {}
for i in range(1,14):
    weevil = Magazine(issue_number=i)
    weevils[i] = weevil
    weevil.save()

conn = MySQLdb.connect(host='127.0.0.1', user='weevil', passwd=getpass.getpass(), db='weevil') 
c = conn.cursor()
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
            text = row[3].decode('latin-1')
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
