from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'registration': reverse('registration', request=request, format=format),
        # 'authorisation': reverse('auth1', request=request, format=format),
    })