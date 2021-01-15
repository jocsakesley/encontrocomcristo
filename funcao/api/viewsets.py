from rest_framework.viewsets import ModelViewSet
from .serializers import FuncaoSerializer
from funcao.models import Funcao

class FuncaoViewSet(ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

