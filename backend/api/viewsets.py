from rest_framework import viewsets
from rest_framework import permissions
from .models import PnpAcademicos
from .serializers import PNPSerializer, YearSerializer, InstitutionSerializer


class PNPViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PnpAcademicos.objects.all()
    serializer_class = PNPSerializer


class YearViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PnpAcademicos.objects.values('pnp_aca_ano').distinct()
    serializer_class = YearSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PnpAcademicos.objects.values('pnp_aca_instituicao_sigla').distinct()
    serializer_class = InstitutionSerializer
