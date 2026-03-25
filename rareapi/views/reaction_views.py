from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rareapi.authentication import RareAuthentication
from rareapi.models import Reaction


@api_view(['GET', 'POST'])
@authentication_classes([RareAuthentication])
@permission_classes([IsAuthenticated])
def reaction_list(request):
    if request.method == 'POST':
        if not request.user.is_staff:
            return Response({'error': 'Forbidden'}, status=403)
        reaction = Reaction.objects.create(
            label=request.data.get('label'),
            image_url=request.data.get('image_url')
        )
        return Response({'id': reaction.id, 'label': reaction.label, 'image_url': reaction.image_url}, status=201)

    reactions = Reaction.objects.order_by('label')
    data = [{'id': r.id, 'label': r.label, 'image_url': r.image_url} for r in reactions]
    return Response(data)
