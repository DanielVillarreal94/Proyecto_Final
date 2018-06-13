from django.urls import path, include
from rol import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('docente_rest', views.DocenteViewSet)
router.register('materia_rest', views.MateriaViewSet)
router.register('estudiante_rest', views.EstudianteViewSet)
router.register('nota_rest', views.NotaViewSet)


urlpatterns = [
    path('api/',include(router.urls)),    
    path('',views.first_view,name='base'),
    path ('nota/', views.NotaListView.as_view(), name='nota-list'),
    path('nota/create/', views.NotaCreate.as_view(), name='nota-create'),
    path('nota/<int:pk>/update/',views.NotaUpdate.as_view(),name='nota-update'),
    #path('nota/<int:pk>/detail/',views.NotaDetailView.as_view(),name='nota-detail'),
    ##########materia
    path('materia/create/', views.MateriaCreate.as_view(), name='materia-create'),
    ############docente
    path('docente/create/', views.DocenteCreate.as_view(), name='docente-create'),
    path('docente/<int:pk>/detail/',views.DocenteDetailView.as_view(),name='docente-detail'),
    path('docente/', views.DocenteListView.as_view(), name='docente-list'),
    path('docente/<int:pk>/update/',views.DocenteUpdate.as_view(),name='docente-update'),
    path('docente/<int:pk>/delete/', views.DocenteDelete.as_view(), name='docente-delete'),
]
