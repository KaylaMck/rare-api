from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rareapi.authentication import RareAuthentication
from rareapi.models import Category


@api_view(['GET'])
@authentication_classes([RareAuthentication])
@permission_classes([IsAuthenticated])
def category_list(request):
    categories = Category.objects.order_by('label')
    data = [{'id': c.id, 'label': c.label} for c in categories]
    return Response(data)
