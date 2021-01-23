from rest_framework import serializers
from participantes.models import Participante
from funcao.api.serializers import FuncaoSerializer
from funcao.models import Funcao

class ParticipantesSerializer(serializers.ModelSerializer):
    funcao = FuncaoSerializer()
    class Meta:
        model = Participante
        fields = '__all__'

    def create(self, validated_data):
        funcao = validated_data['funcao']
        del validated_data['funcao']

        participantes = Participante.objects.create(**validated_data)
        fun = Funcao.objects.create(**funcao)
        participantes.funcao = fun

        return participantes

    def update(self, instance, validated_data):
        funcao = validated_data.pop("funcao")
        list_dict = []
        for f in funcao.items():
            list_dict.append(f)
        print(dict(list_dict))
        fun = Funcao.objects.get_or_create(funcao=list_dict[0][1], descricao=list_dict[1][1], defaults=dict(list_dict))
        print(type(fun), fun[0].pk)
        instance.funcao = fun[0]
        instance.nome = validated_data.get('nome', instance.nome)
        instance.sobrenome = validated_data.get('sobrenome', instance.sobrenome)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.nascimento = validated_data.get('nascimento', instance.nascimento)
        instance.sexo = validated_data.get('nome', instance.sexo)
        instance.email = validated_data.get('email', instance.email)
        instance.telefone = validated_data.get('telefone', instance.nome)
        instance.endereco = validated_data.get('endereco', instance.endereco)
        instance.evangelico = validated_data.get('evangelico', instance.evangelico)
        instance.igreja = validated_data.get('igreja', instance.igreja)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.save()



        return instance
        

