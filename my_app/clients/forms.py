from django import forms
from graphene_django.forms.mutation import DjangoFormMutation
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_django import DjangoObjectType
from .models import Client
import graphene


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('nombre', 'edad')

# This will get returned when the mutation completes successfully
class ClientType(DjangoObjectType):
    class Meta:
        model = Client

class ClientMutation(DjangoModelFormMutation):
    client = graphene.Field(ClientType)
    
    class Meta:
        form_class = ClientForm
