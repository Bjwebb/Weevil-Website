# This files deals with the old site's urls and redirects them appropriately

from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from weevil.models import Article

category_mapping = {
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

flat_mapping = {
    169: '/committee/getting-involved/', 
    272: '/committee/constitution/',
    # /committee/contact/
    177: '/supporters/',
    178: '/supporters/cusu-reprographics/'
}

committee_mapping = {
    168: 2013,
    392: 2012,
    274: 2011
}

def redirect(request):
    if request.GET.get('view') == 'category':
        id_ = int(request.GET.get('id').split(':')[0])
        if id_ in category_mapping:
            return HttpResponseRedirect(reverse('weevil.views.magazine', args=(category_mapping[id_],)))
    elif request.GET.get('view') == 'article':
        id_ = int(request.GET.get('id').split(':')[0])
        if id_ in flat_mapping:
            return HttpResponseRedirect(flat_mapping[id_])
        elif id_ in committee_mapping:
            return HttpResponseRedirect(reverse('weevil.views.committee', args=(committee_mapping[id_],)))
        else:
            article = Article.objects.get(legacy_id=id_)
            if article:
                return HttpResponseRedirect(reverse('weevil.views.article', args=(article.magazine.issue_number, article.slug)))
    raise Http404
