# aqui sera a parte de criação de banco de dados dos exercicios
#nomes, descrição, grupo muscular, e instruçẽos
from django.db import models


class Exercicio(models.Model):

    GRUPOS_MUSCULARES = [
        ('PEITO', 'Peito'),
        ('COSTAS', 'Costas'),
        ('PERNAS', 'Pernas'),
        ('OMBROS', 'Ombros'),
        ('BRACOS', 'Braços'),
        ('ABDOMEN', 'Abdômen'),
    ]
#cada exercício terá um campo de texto chamado nome,
#com no máximo 100 caracteres
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    grupo_muscular = models.CharField(
        max_length=20,
        choices=GRUPOS_MUSCULARES
    )