from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Cargo, Funcionario, Depoimento, Servico
from .forms import ContactModelForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class=ContactModelForm
    success_url=reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['depoimentos'] = Depoimento.objects.order_by('?').all()
        context['servicos'] = Servico.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        form.save()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
    	messages.error(self.request, 'Não foi possível enviar o E-mail')
    	return super(IndexView, self).form_invalid(form, *args, **kwargs)