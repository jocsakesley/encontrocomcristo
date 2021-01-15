from rest_framework.viewsets import ModelViewSet
from .serializers import ParticipantesSerializer
from participantes.models import Participante


class ParticipantesModelViewSet(ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipantesSerializer