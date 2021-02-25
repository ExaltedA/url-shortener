
from django.http import HttpResponseRedirect,HttpResponse

from rest_framework import  status
from rest_framework.decorators import api_view

from .serializers import *



@api_view(['GET'])
def getFullUrl(request, short_url):
    url = Url.objects.filter(url_hash=short_url)
    if url:
        url[0].clicked()
        return HttpResponseRedirect(url[0].full_url)
    else:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
