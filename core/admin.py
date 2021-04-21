from django.contrib import admin
from .models import Cargo, Funcionario, Depoimento, Contato, Servico
# Register your models here.

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
	list_display = ('cargo', 'active', 'modified_at')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('cargo', 'nome', 'modified_at')

@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'profissao', 'modified_at')

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
	list_display = ('name', 'subject', 'modified_at')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'texto', 'modified_at')