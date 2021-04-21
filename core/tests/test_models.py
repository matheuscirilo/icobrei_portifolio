import uuid 
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path

class get_file_path_TastCase(TestCase):

    def setUp(self):
         self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class Pessoa_Juridica_TestCase(TestCase):

	def setUp(self):
		self.pessoa_juridica = mommy.make('Pessoa_Juridica')

	def test_str(self):
		self.assertEquals(str(self.pessoa_juridica), self.pessoa_juridica.razao_social)