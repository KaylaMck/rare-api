from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rareapi.authentication import RareAuthentication
from rareapi.models import Category


@api_view(['GET', 'POST'])
@authentication_classes([RareAuthentication])
@permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == 'POST':
        category = Category.objects.create(label=request.data.get('label'))
        return Response({'id': category.id, 'label': category.label}, status=201)

    categories = Category.objects.order_by('label')
    data = [{'id': c.id, 'label': c.label} for c in categories]
    return Response(data)


@api_view(['GET', 'PUT'])
@authentication_classes([RareAuthentication])
@permission_classes([IsAuthenticated])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)

    if request.method == 'GET':
        return Response({'id': category.id, 'label': category.label})

    if request.method == 'PUT':
        category.label = request.data.get('label', category.label)
        category.save()
        return Response({'id': category.id, 'label': category.label})
