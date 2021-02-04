from rest_framework import serializers
from equipes.models import Equipe
from funcao.models import Funcao
from participantes.api.serializers import ParticipantesSerializer
from participantes.models import Participante

class EquipesSerializer(serializers.ModelSerializer):
    lider = ParticipantesSerializer()
    membros = ParticipantesSerializer(many=True)
    class Meta:
        model = Equipe
        fields = "__all__"

    def cria_membros(self, membros, equipes):
        for membro in membros:
            funcao = membro['funcao']
            del membro['funcao']

            func = Funcao.objects.get_or_create(**funcao)[0]
            membro['funcao'] = func
            mb = Participante.objects.get_or_create(**membro)[0]
            print(mb)
            equipes.membros.add(mb)

    def create(self, validated_data):
        print(dict(validated_data['lider']))
        lider = validated_data['lider']
        del validated_data['lider']
        membros = validated_data['membros']
        del validated_data['membros']


        equipes = Equipe.objects.create(**validated_data)
        self.cria_membros(membros, equipes)
        funcao = dict(lider)
        funcao = dict(funcao['funcao'])
        print(funcao)

        func = Funcao.objects.get_or_create(**funcao)[0]
        lider = dict(lider)
        lider['funcao'] = func

        lid = Participante.objects.get_or_create(**lider)[0]
        equipes.lider = lid
        equipes.save()
        return equipes

    #def update(self, instance, validated_data):