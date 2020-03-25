from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.http.response import JsonResponse



class Index(View):
    def get(self, request, next='sabe'):
        context = {}
        print("here",request.user.is_authenticated)
        if request.user.is_authenticated:
            context = {
                'is_authenticated': request.user.is_authenticated
            }
        return render(request, "index.html", context)

    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return render(request, "index.html", {})
        else:
            usuario = ""
            pasword = ""
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                context = {
                    'is_authenticated': request.user.is_authenticated
                }
                return render(request, "index.html", context)
            else:
                return render(request, "index.html", context)

class Login(View):
    def post(self, request):
        print(request.POST)
        username = request.POST['nombre']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("user ", user)
        if user is not None:
            login(request, user)
            print("user", user.is_authenticated)
            return HttpResponseRedirect(reverse('clients:index'))
        else:
            return HttpResponse("bad authentication")

class Logout(View):
    def post(self, request):
        print("in logout ", request.user)
        logout(request)
        return HttpResponseRedirect(reverse('main:index'))


class Item(View):
    def get(self, request):
        response = JsonResponse({'foo': 'bar'})
        return response
