from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
import uuid
# Create your models here.

def get_file_path(_instance, filename):
	ext = filename.split('.')[-1]
	filename = f'{uuid.uuid4()}.{ext}'
	return filename

class Base(models.Model):

	created_at = models.DateField(
		'Data de Criação',
		auto_now_add=True
		)

	modified_at = models.DateField(
		'Data de Atualização',
		auto_now=True
		)
		
	active = models.BooleanField(
		'Ativo?',
		default=True
		)

	class Meta:
		
		abstract = True


class Cargo(Base):

	cargo = models.CharField(
		'Cargo',
		max_length=100,
		)

	class Meta:
		
		verbose_name = 'Cargo'	
		verbose_name_plural = 'Cargos'

	def __str__(self):
		return self.cargo

class Funcionario(Base):

	nome = models.CharField(
		'Nome',
		max_length=100,
		)

	cargo = models.ForeignKey(
		'core.Cargo',
		verbose_name='Cargo',
		on_delete=models.CASCADE
		)

	bio = models.TextField(
		'Biografia',
		max_length=200,
		)

	imagem = StdImageField(
		'Imagem',
		upload_to=get_file_path,
		variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}
		)


	linkedin = models.URLField(
		'LinkedIn',
		max_length=100,
		default='#',
		blank=True
		)


	class Meta:
		
		verbose_name = 'Funcionário'	
		verbose_name_plural = 'Funcionários'

	def __str__(self):
		return self.nome

class Depoimento(Base):

	nome = models.CharField(
		'Nome',
		max_length=100,
		)

	profissao = models.CharField(
		'Profissão',
		max_length=100,
		)


	comentario = models.TextField(
		'Comentário',
		max_length=200,
		)

	imagem = StdImageField(
		'Imagem',
		upload_to=get_file_path,
		variations={'thumb': {'width': 75, 'height': 75, 'crop': True}}
		)

	class Meta:
		
		verbose_name = 'Depoimento'	
		verbose_name_plural = 'Depoimentos'

	def __str__(self):
		return self.nome


class Contato(Base):

	name = models.CharField(
		'Nome',
		max_length=100,
	)

	email = models.EmailField(
		'E-mail',
		max_length=150,
	)

	subject = models.CharField(
		'Assunto',
		max_length=150,
	)

	message = models.CharField(
		'Mensagem',
		max_length=1000,
	)

	class Meta:
		
		verbose_name = 'E-mail'	
		verbose_name_plural = 'E-mails'

	def __str__(self):
		return self.name


class Servico(Base):

	nome = models.CharField(
		'Nome',
		max_length=100,
		)

	texto = models.TextField(
		'Texto',
		max_length=200,
		)

	CHOISE_ICONES = {
		('lni-cog', 'Engrenagem'),
		('lni-stats-up', 'Gráfico'),
		('lni-users', 'Usuário'),
		('lni-layers', 'Design'),
		('lni-mobile', 'Mobile'),
		('lni-rocket', 'Foguete')
		}


	icone = models.CharField(
		'icone',
		max_length=100,
		choices=CHOISE_ICONES,
		)

	class Meta:
		
		verbose_name = 'Serviço'	
		verbose_name_plural = 'Serviços'

	def __str__(self):
		return self.nome
