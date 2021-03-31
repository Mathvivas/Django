from django.contrib import admin
from .models import Receita

# Terminal: python manage.py createsuperuser

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria')     # Mostra a lista de receitas no admin
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)       # Precisa de uma vírgula, pois necessita de uma lista ou tupla
    list_filter = ('categoria',)
    # Paginação
    list_per_page = 10


admin.site.register(Receita, ListandoReceitas)
