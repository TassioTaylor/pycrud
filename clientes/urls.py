from django.urls import path
from . import views as v

app_name ='clientes'

urlpatterns = [

    path('', v.clientes_List, name='clientes_list'),
    path('cadastrar/', v.ClienteCreate.as_view(), name='cliente_cadastrar'),
    path('deletar/<int:pk>', v.ClienteDelete.as_view(), name='cliente_deletar'),
    path('editar/<int:pk>', v.ClienteUpdate.as_view(), name='cliente_editar'),



]
