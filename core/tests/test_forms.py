from django.test import TestCase
from core.forms import ContactForm

class ContactFormTestcase(TestCase):

	def setUp(self):
		self.name = 'Matheus'
		self.email = 'matheus@gmail.com'
		self.subject = 'Oi'
		self.message = 'Bom dia'

		self.dados = {
	        'name': self.name,
	    	'email': self.email,
	    	'subject': self.subject,
	    	'message': self.message,
	    }

		self.form = ContactForm(data=self.dados)

		def test_send_mail(self):
			form1 = ContactForm(data=self.dados)
			form1.is_valid()
			res1 = form1.send_mail()

			form2 = self.form
			form2.is_valid()
			res2 = form2.send_mail()

			self.assertEquals(res1, res2)