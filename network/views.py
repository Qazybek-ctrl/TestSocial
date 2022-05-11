from django.shortcuts import render
from .models import SocialPerson
# Create your views here.

def index(request):
    person = SocialPerson.objects.get(user=request.user.id)
    context = {
        'person': person,
        'back' : f'background: url("{person.background.url}") top center;'
    }
    return render(request, 'network/index.html', context)

def unauthorized_access(request):
    return render(request, 'network/unatrac.html')