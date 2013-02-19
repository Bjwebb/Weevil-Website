from weevil.models import Magazine

def menu(request):
    return {'weevils':Magazine.objects.order_by('-issue_number')}
