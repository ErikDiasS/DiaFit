from django.contrib import admin
from .models import Exercicio


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):

    list_display = ('nome', 'grupo_muscular')

    list_filter = ('grupo_muscular',)

    search_fields = ('nome',)
