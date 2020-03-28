import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from graphene import relay, Schema
from .models import Client, Travel
from graphene_django.forms.mutation import DjangoFormMutation
from django import forms
from graphene_django.rest_framework.mutation import SerializerMutation
from .serializers import ClientSerializer


class ClientType(SerializerMutation):
    class Meta:
        serializer_class = ClientSerializer

class ClientConnection(relay.Connection):
    class Meta:
        node = ClientType

class TravelType(DjangoObjectType):
    class Meta:
        model = Travel

class Query(object):
    all_clients = relay.ConnectionField(ClientConnection)
    all_travels = graphene.List(TravelType)

    client = graphene.Field(ClientType,
                                id=graphene.Int(),
                                nombre=graphene.String())
    
    travel = graphene.Field(TravelType,
                                  id=graphene.Int(),
                                  mes=graphene.String())

    def resolve_all_clients(self, info, **kwargs):
        return Client.objects.all()

    def resolve_all_travels(self, info, **kwargs):
        return Travel.objects.all()
    
    def resolve_client(self, info, **kwargs):
          id = kwargs.get('id')
          nombre = kwargs.get('nombre')

          if id is not None:
              return Client.objects.get(pk=id)

          if nombre is not None:
              return Client.objects.get(nombre=nombre)

          return None

    def resolve_travel(self, info, **kwargs):
        id = kwargs.get('id')
        mes = kwargs.get('mes')
        if id is not None:
            return Travel.objects.get(pk=id)
        if mes is not None:
            return Travel.objects.get(mes=mes)
        return None

class UpdateClient(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        id = graphene.ID()

    client = graphene.Field(ClientType)

    def mutate(self, info, nombre, id):
        client = Client.objects.get(pk=id)
        client.nombre = nombre
        client.save()
        return UpdateClient(client=client)

class CreateClient(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        nombre = graphene.String()
        edad = graphene.String()

    # The class attributes define the response of the mutation
    client = graphene.Field(ClientType)

    def mutate(self, info, nombre, edad):
        client = Client.objects.create(nombre=nombre, edad=edad)
        client.save()
        # Notice we return an instance of this mutation
        return CreateClient(client=client)


class MyMutations(object):
    update_client = UpdateClient.Field()
    #create_client = CreateClient()
