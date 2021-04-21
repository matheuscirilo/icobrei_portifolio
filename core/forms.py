from django import forms
from django.core.mail.message import EmailMessage
from .models import Contato

class ContactModelForm(forms.ModelForm):
	
	class Meta:

		model = Contato
		fields = ['name', 'email', 'subject', 'message']
 

	def send_mail(self):
		name = self.cleaned_data['name']
		email = self.cleaned_data['email']
		subject = self.cleaned_data['subject']
		message = self.cleaned_data['message']

		contents = f'Nome: {name}\nE-mail: {email}\nAssunto: {subject}\nMensagem: {message}'

		mail = EmailMessage(
			subject=subject,
			body=contents,
			from_email='contato@icobrei.com.br',
			to=['contato@seudominio.com.br', ],
			headers={'Reply-To': email}
		)
		mail.send()

