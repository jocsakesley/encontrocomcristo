from rest_framework.viewsets import ModelViewSet
from .serializers import EquipesSerializer
from equipes.models import Equipe

class EquipesViewSet(ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipesSerializer