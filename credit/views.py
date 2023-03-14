from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Client, Credit, Account


class Clientlist(generic.ListView):
    model = Client
    template_name = 'clientlist.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return self.model.objects.all()


class ClientDetail(generic.DetailView):
    model = Client
    template_name = 'client_detail.html'
