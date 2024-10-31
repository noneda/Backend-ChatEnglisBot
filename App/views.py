from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from .models import MessageBot
from .serializers import MessageBotSerializer
# Create your views here.


@api_view(['GET'])
def rootData(req):
    set = {
        'name' :'ChatEnglish',
        'author' :'noneda',
    }
    return Response(set)


@api_view(['POST'])
def botMessage(req):
    set = req.data.get('set')