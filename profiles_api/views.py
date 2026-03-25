from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test API View"""
    def get(self,request,format=None):
        """  Returns a list of API views feature"""

        an_apiview =[
            'uses HTTP methods as function (get, post , patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application post',
            'Is mapped manuallu to Urls'
        ]

        return Response({'message':'Hello','an api view':an_apiview})

