from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('reporte/', views.report, name='reporte'),
    path('clientes/', views.client_list, name='clientes'),
    path('ventas/', views.sale_list, name='ventas'),
    path('', RedirectView.as_view(url='reporte/'), name='index'),
]