#traz para o arquivo as ferramentas que usaremos para criar campos e modelos do banco.
#traz a estrutura de usuário que o próprio Django já criou.

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # Tipos de usuário permitidos no Dia Fit.
    TIPO_ALUNO = 'ALUNO'
    TIPO_PROFESSOR = 'PROFESSOR'


    TIPOS_USUARIO = [
        (TIPO_ALUNO, 'Aluno'),
        (TIPO_PROFESSOR, 'Professor'),
    ]

    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPOS_USUARIO,
        default=TIPO_ALUNO,
    )
class ProfessorAluno(models.Model):

    professor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='alunos'
)
    aluno = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name= 'professor',
        null=True,
        blank=True
    )