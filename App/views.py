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
    if not set:
        return Response({
                "error" : "data don't found!!!", 
            }, 
            status=status.HTTP_400_BAD_REQUEST
        );
    
    post = MessageBot(user_input = set)
    post.save()
    
    get = MessageBotSerializer(post)
    return Response(
        get.data, status=status.HTTP_201_CREATED
    )