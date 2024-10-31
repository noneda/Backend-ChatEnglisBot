from rest_framework.decorators import api_view
from django.http.response import JsonResponse

# Create your views here.


@api_view(['GET'])
def rootData(req):
    set = {
        'name' :'ChatEnglish',
        'author' :'noneda',
    }
    return JsonResponse(set)

