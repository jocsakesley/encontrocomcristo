from rest_framework import serializers
from funcao.models import Funcao

class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = '__all__'