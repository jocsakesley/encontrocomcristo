from rest_framework import serializers
from equipes.models import Equipe
from participantes.api.serializers import ParticipantesSerializer
class EquipesSerializer(serializers.ModelSerializer):
    lider = ParticipantesSerializer()
    membros = ParticipantesSerializer(many=True)
    class Meta:
        model = Equipe
        fields = "__all__"