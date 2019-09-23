from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView

from .forms import ClienteForm
from .models import Cliente


def index(request):
    return HttpResponse("TESTE")


def clientes_List(request):
    template_name = 'clientes_list.html'
    objects = Cliente.objects.all()
    context = {'object_list': objects}

    return render(request, template_name, context)


def cliente_cadastrar(request):
    form = ClienteForm()
    template_name = 'cliente_form.html'

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cliente_list.html'))
    context = {'form': form}
    return render(request, template_name, context)


class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'
    form_class = ClienteForm


class Clientedelete(DeleteView):
    template_name = 'cliente_confirm_delete.html'
    model = Cliente
    success_url = reverse_lazy('clientes:clientes_list')
