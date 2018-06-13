from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.shortcuts import render
#from .models import Estudiante, Nota
from django.contrib.auth.decorators import login_required
from .models import Docente, Materia, Estudiante, Nota
from rest_framework import viewsets
from django.urls import reverse_lazy 
from .serializers import EstudianteSerializer, MateriaSerializer, DocenteSerializer, NotaSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



#######################REST
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer


class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer


############################################################
@login_required
def first_view(request):
    #return HttpResponse("<H1>HOLA MUNDO DESDE LA VISTA first_view</H1>")
    return render(request, 'base.html')
############################################################
@method_decorator(login_required, name='dispatch')
class NotaListView(ListView):
    model = Nota

class NotaUpdate(UpdateView):
    model = Nota
    fields = '__all__'

class NotaCreate(CreateView):
    model = Nota
    fields = '__all__'

class NotaDetailView(DetailView):
    model = Nota

############MATERIA
class MateriaListView(ListView):
    model = Materia

class MateriaUpdate(UpdateView):
    model = Materia
    fields = '__all__'

class MateriaCreate(CreateView):
    model = Materia
    fields = '__all__'

class MateriaDetailView(DetailView):
    model = Materia
    fields = '__all__'


#####################PROFESOR

class DocenteCreate(CreateView):
    model = Docente
    fields = '__all__'

class DocenteDelete(DeleteView):
    model = Docente
    success_url = reverse_lazy('docente-list')

class DocenteDetailView(DetailView):
    model = Docente


class DocenteUpdate(UpdateView):
    model = Docente
    fields = '__all__'

class DocenteListView(ListView):
    model = Docente

def students(request):
    all_students=Estudiante.objects.all()
    context={'object_list': all_students}
    return render(request, 'rol/allstudents.html',context)