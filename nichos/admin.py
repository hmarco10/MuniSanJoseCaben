from django.contrib import admin
from .models import Propietario, Predio, Reservation


# Register your models here.
@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dpi', 'telefono', 'direccion')


@admin.register(Predio)
class PredioAdmin(admin.ModelAdmin):
    list_display = ('largo', 'ancho', 'nomenclatura')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('titular', 'espacios', 'niveles', 'ornato', 'cancelado', 'inspeccion', 'fecha', 'propietario', 'predio')

