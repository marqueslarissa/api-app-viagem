from django.contrib import admin
from .models import Cliente, Reserva, Hotel, Voo

admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Hotel)
admin.site.register(Voo)
