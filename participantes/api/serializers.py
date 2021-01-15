from rest_framework import serializers
from participantes.models import Participante
from funcao.api.serializers import FuncaoSerializer

class ParticipantesSerializer(serializers.ModelSerializer):
    funcao = FuncaoSerializer()
    class Meta:
        model = Participante
        fields = '__all__'