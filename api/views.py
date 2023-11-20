from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def test_data(request):
    person = {'name':'Ridwan Halim', 'age':20}
    return Response(person)