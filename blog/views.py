import json
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
    "Name" : "Olamide Komolafe",
    "Track" : "Backend(Python)",
    "Message" : "Hi, mentor, you're doing a great job"

    }
    dump = json.dumps(data)
    return HttpResponse(dump, content_type = 'application/json')

