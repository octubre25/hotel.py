from django.urls import path

from .views import *


app_name="tienda"

urlpatterns = [
	path('clientes/', listar_clientes, name= 'listar_clientes'),
	path('habitaciones/', listar_habitaciones, name= 'listar_habitaciones'),
	path(
			'habitaciones/ocupadas',
			listar_habitaciones_ocupadas,
			name= 'listar_habitaciones_o'
		),
	path(
			'facturas/',
			listar_encabezado_factura,
			name= 'listar_facturas'
		),
	path(
			'facturas/<uuid:uuid_factura>',
			ver_factura,
			name= 'ver_factura'
		),
	
	path(
			'facturas/filtrar/fecha',
			listar_facturas_rango,
			name= 'listar_facturas_rango'
		),
]