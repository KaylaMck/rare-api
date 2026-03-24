from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rareapi.authentication import RareAuthentication
from rareapi.models import Tag


@api_view(['GET', 'POST'])
@authentication_classes([RareAuthentication])
@permission_classes([IsAuthenticated])
def tags(request):
    if request.method == 'GET':
        all_tags = Tag.objects.order_by('label')
        tag_list = [{'id': tag.id, 'label': tag.label} for tag in all_tags]
        return Response(tag_list)

    if request.method == 'POST':
        new_tag = Tag.objects.create(label=request.data.get('label'))
        return Response({'id': new_tag.id, 'label': new_tag.label}, status=201)
