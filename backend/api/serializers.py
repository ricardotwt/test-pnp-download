from rest_framework import serializers
from .models import PnpAcademicos

class PNPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PnpAcademicos
        fields = '__all__'

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = PnpAcademicos
        fields = ['pnp_aca_ano']

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PnpAcademicos
        fields = ['pnp_aca_instituicao_sigla']