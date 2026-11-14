# Importa as ferramentas necessárias para trabalhar com o painel administrativo.
from django.contrib import admin

# Importa a estrutura administrativa de usuários que o próprio Django oferece.
# Assim, aproveitamos funcionalidades prontas, como edição de senha e permissões.
from django.contrib.auth.admin import UserAdmin

# Importa os modelos de usuário e relacionamento que criamos no arquivo models.py.
from .models import User, ProfessorAluno


# Registra nosso modelo User no painel administrativo do Django.
# O decorador @admin.register permite associar o modelo à classe administrativa.
@admin.register(User)
class DiaFitUserAdmin(UserAdmin):

    # O fieldsets organiza os campos exibidos na tela de edição do usuário.
    # UserAdmin.fieldsets mantém todos os campos originais do Django.
    # Depois, adicionamos uma nova seção chamada "Informações do Dia Fit".
    # Nela, colocamos nosso campo personalizado tipo_usuario.
    fieldsets = UserAdmin.fieldsets + (
        ('Informações do Dia Fit', {
            'fields': ('tipo_usuario',),
        }),
    )

    # Define quais informações serão exibidas na listagem de usuários.
    # Isso facilita a identificação e o gerenciamento das contas.
    list_display = (
        'username',      # Nome de usuário utilizado para entrar no sistema.
        'first_name',    # Primeiro nome do usuário.
        'last_name',     # Sobrenome do usuário.
        'email',         # Endereço de e-mail.
        'tipo_usuario',  # Identifica se é aluno ou professor.
        'is_active',     # Informa se a conta está ativa.
    )

    # Cria filtros laterais na listagem de usuários.
    # Assim, podemos visualizar somente alunos, professores ou contas ativas.
    list_filter = ('tipo_usuario', 'is_active')


# Registra o modelo ProfessorAluno no painel administrativo.
# Esse modelo representa o vínculo entre professores e alunos.
@admin.register(ProfessorAluno)
class ProfessorAlunoAdmin(admin.ModelAdmin):

    # Define as colunas que aparecerão na listagem dos relacionamentos.
    # Poderemos visualizar qual professor está associado a qual aluno.
    list_display = (
        'professor',
        'aluno',
    )

    # Cria um filtro para facilitar a busca dos alunos de cada professor.
    list_filter = ('professor',)