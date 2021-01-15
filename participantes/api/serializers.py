from rest_framework import serializers
from participantes.models import Participante

class ParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'