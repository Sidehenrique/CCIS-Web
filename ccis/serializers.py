from rest_framework import serializers
from .models import Card, enderecoContato, dadosPessoais, profissional, MessageHistory, CardSetorHistory
from django.contrib.auth.models import User, Group


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = enderecoContato
        fields = ['emailCorporativo', 'ramal']


class DadosPessoaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = dadosPessoais
        fields = ['nomeCompleto', 'sexo', 'foto', 'cpf']


class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = profissional
        fields = ['cargo', 'area', 'paUnidade']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class MessageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageHistory
        fields = '__all__'


class CardSetorHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CardSetorHistory
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):

    solicitante = CustomUserSerializer()
    responsavel = CustomUserSerializer(allow_null=True)

    solicitante_contato = ContatoSerializer(source='solicitante.enderecoContato', read_only=True)
    solicitante_dados_pessoais = DadosPessoaisSerializer(source='solicitante.dadosPessoais', read_only=True)
    solicitante_profissional = ProfissionalSerializer(source='solicitante.profissional', read_only=True)

    responsavel_contato = ContatoSerializer(source='responsavel.enderecoContato', read_only=True)
    responsavel_dados_pessoais = DadosPessoaisSerializer(source='responsavel.dadosPessoais', read_only=True)
    responsavel_profissional = ProfissionalSerializer(source='responsavel.profissional', read_only=True)

    messages = MessageHistorySerializer(many=True, read_only=True, source='messagehistory_set')
    setor_history = CardSetorHistorySerializer(many=True, read_only=True, source='cardsetorhistory_set')

    class Meta:
        model = Card
        fields = '__all__'

