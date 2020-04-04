from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client, Travel
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.contrib.auth.decorators import login_required #permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
import json
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer

from graphene_django.forms.mutation import DjangoFormMutation
from django import forms
from .forms import ClientForm




class PublisherList(ListView):
    paginate_by = 2
    model = Client



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

@method_decorator(login_required, name='dispatch')
class Index(View):
    permission_required = ()
    #permission_required = ('clients.view_client')
    def get(self, request):
        clients = Client.objects.all()
        travels = Travel.objects.all()
        users = User.objects.all()
        print("inspect users ", users)
        paginator = Paginator(clients, 2)
        page_number = 0
        if request.GET.get('page'):
            page_number = int(request.GET.get('page'))
        page_obj = paginator.get_page(page_number)
        pages = paginator.num_pages
        context = {
            'is_authenticated': request.user.is_authenticated,
            'clientes': clients,
            'clientes': page_obj,
            'travels': travels,
            'pages': pages,
            'current_page': page_number,
            'previous_page': page_number-1,
            'next_page': page_number+1
        } 
        return render(request, "clients/index.html", context)

    #@permission_required('polls.add_choice', raise_exception=True)
    def post(self, request):
        print("entro")
        print(request.POST)
        nombre = request.POST['nombre']
        password = request.POST['password']
        user = User.objects.create(username=nombre, password=password)
        user.save()
        return HttpResponse("usign class viewss")

    def put(self, request):
        print("en el put")
        json_val = json.loads(request.body)
        client = Client.objects.filter(nombre=json_val['user'])[0]
        print("client", client.edad)
        Client.objects.filter(pk=client.pk).update(edad=json_val['password'])
        return HttpResponse("usign class viewss")

#def index(request):
#    clients = Client.objects.all()
#    travels = Travel.objects.all()
#    context = {
#        'clientes': clients,
#        'travels': travels
#    }
#    if request.method == "POST":
#        print("entro")
#        print(request.POST)
#        nombre = request.POST['nombre']
#        client = Client.objects.create(nombre = nombre, edad = 30 )
#        client.save()
#        return HttpResponse("Hello, world. You're at the polls index.")
#    else:
#        return render(request, "clients/index.html", context)


def bio(request, id=0):
    try:
        client = Client.objects.get(id=id)
        travels = Travel.objects.filter(Client=client)
        context = {
            'client': client,
            'travels': travels
        }
        return render(request, "clients/detail.html", context)
    except ObjectDoesNotExist:
        return HttpResponse("no existe {}".format("so"))


class MorningGreetingView(View):
    greeting = "Morning to ya"
    def get(self, request):
        #return HttpResponse("hey {}".format(self.greeting))
        return render(request, "index.html", {})


def get_client(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ClientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form)
            nombre = form.cleaned_data['nombre']
            print("viendo el nombre", nombre)
            return HttpResponse("bien")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientForm()

    return render(request, 'graph_form.html', {'form': form})

