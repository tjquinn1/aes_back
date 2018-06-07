from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from . import forms
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
import random
import string
from django.contrib import messages
from rest_framework import viewsets
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import CreateAPIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer


def custom_login(request):
    form = forms.CustomLoginForm()
    
    if request.method == 'POST':
        form = forms.CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, "Welcome {}".format(request.user.first_name))
                return HttpResponseRedirect('/login_success/')
            else:
                messages.error(request, "Your user name or password is incorect")
    return render(request, 'registration/login.html', {'form': form})





def logout_view(request):
    logout(request)
    return redirect("/home/")

'''
class SignUp(APIView):
    def post(self, request, format=None):
        form_class = forms.UserCreateForm
        success_url = "accounts/pre/"
        #template_name = "accounts/signup.html"
        def form_valid(self, form):
            valid = super(SignUp, self).form_valid(form)
            email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
            new_user = authenticate(email=email, password=password)
            auth_login(self.request, new_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
'''

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

@login_required    
def Edit(request): 
    form = forms.UserCreateForm(instance=request.user)
    
    if request.method == 'POST':
        form = forms.UserCreateForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated {}".format(form.cleaned_data['name']))
            return HttpResponseRedirect('/')
    return render(request, 'accounts/signup.html', {'form': form})

