# Importa as ferramentas para criar modelos e campos no banco de dados.
from django.db import models

# Importa a estrutura de usuário que o Django já oferece.
from django.contrib.auth.models import AbstractUser

# Importa a ferramenta para validar informações e apresentar erros.
from django.core.exceptions import ValidationError


# Cria nosso modelo de usuário personalizado.
# Aproveitamos os campos e funcionalidades do usuário padrão do Django.
class User(AbstractUser):

    # Define os tipos de usuários permitidos no Dia Fit.
    TIPO_ALUNO = 'ALUNO'
    TIPO_PROFESSOR = 'PROFESSOR'

    # Relaciona o valor armazenado no banco com o nome exibido no sistema.
    TIPOS_USUARIO = [
        (TIPO_ALUNO, 'Aluno'),
        (TIPO_PROFESSOR, 'Professor'),
    ]

    # Cria um campo para identificar se o usuário é aluno ou professor.
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPOS_USUARIO,
        default=TIPO_ALUNO,
    )


# Cria o modelo responsável pelo relacionamento entre professor e aluno.
class ProfessorAluno(models.Model):

    # Relaciona um professor ao usuário cadastrado no sistema.
    # CASCADE significa que, se o usuário for excluído,
    # os relacionamentos associados também serão excluídos.
    professor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='alunos'
    )

    # Relaciona um aluno ao professor.
    # null=True permite que o campo fique vazio no banco.
    # blank=True permite que o campo fique vazio nos formulários.
    aluno = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='professor',
        null=True,
        blank=True
    )

    # Configura como o modelo será apresentado no Django Admin.
    class Meta:

        # Nome apresentado quando o modelo estiver no singular.
        verbose_name = 'Professor e aluno'

        # Nome apresentado quando o modelo estiver no plural.
        verbose_name_plural = 'Professores e alunos'

    # Verifica se os usuários selecionados possuem os tipos corretos.
    def clean(self):

        # Confere se o usuário escolhido como professor
        # realmente está cadastrado como PROFESSOR.
        if self.professor.tipo_usuario != User.TIPO_PROFESSOR:
            raise ValidationError(
                'O usuário selecionado como professor deve ser um PROFESSOR'
            )

        # Se existir um aluno, verifica se ele está cadastrado como ALUNO.
        if self.aluno and self.aluno.tipo_usuario != User.TIPO_ALUNO:
            raise ValidationError(
                'O usuário selecionado como aluno deve ser um ALUNO'
            )

    # Personaliza o processo de salvamento do relacionamento.
    def save(self, *args, **kwargs):

        # Executa as validações antes de salvar no banco de dados.
        self.full_clean()

        # Executa o salvamento original do Django.
        super().save(*args, **kwargs)