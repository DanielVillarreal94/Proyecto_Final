from rest_framework import serializers
from .models import Docente, Materia, Estudiante, Nota

class DocenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Docente
        fields = ('__all__')

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ('__all__')

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('__all__')

class NotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nota
        fields = ('__all__')