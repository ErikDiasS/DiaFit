#traz para o arquivo as ferramentas que usaremos para criar campos e modelos do banco.
#traz a estrutura de usuário que o próprio Django já criou.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

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
    #valida o tipo de usuario se é professor ou aluno
    def clean(self):
        if self.professor.tipo_usuario != User.TIPO_PROFESSOR:
            raise ValidationError(
                'O usuário selecionado como professor deve ser um PROFESSOR'
            )

        if self.aluno and self.aluno.tipo_usuario != User.TIPO_ALUNO:
            raise ValidationError(
                'O usuário selecionado como aluno deve ser um ALUNO'

            )
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        