from django.shortcuts import render,redirect
from .models import TravelModel, GroupModel
from django.views.generic import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.views import generic
from .forms import (LoginForm, UserCreateForm)
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.singing import BadSignature, SignatureExpired, loads. dumps
from django.http import Http404, HttpResposeBadRequest
from django.shortcuts import redirect
from django.template.loader import render_to_string
from .forms import (LoginForm, UserCreateForm)

User = get_user_model()
# Create your views here.

def listview(request):
    object_list = TravelModel.objects.all()
    return render (request, 'list.html', {'object_list' : object_list})

def group_list(request):
    object_list = GroupModel.objects.all()
    return render(request,'group_list.html', {'object_list' : object_list})

class Formview(CreateView):
    template_name = 'form.html'
    model = TravelModel
    fields = ('spot_name','url','useful_review_record')
    success_url = reverse_lazy('list')

class Groupview(CreateView):
    template_name = 'group.html'
    model = GroupModel
    fields = ('group_name','group_password')
    success_url = ('group_list')

def deleteview(request,pk):
    article = TravelModel.objects.get(pk = pk)
    if request.method == 'POST':
        article.delete()
    return redirect('list')

class Editview(UpdateView):
    template_name = 'edit.html'
    model = TravelModel
    fields = ('spot_name','url','useful_review_record')
    success_url = reverse_lazy('list')

class Top(generic.TemplateView):
    template_name = 'top.html'

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'

class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'top.html'


class UserCreate(generic.CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authnticate(username = username, password = password)
            login(request, user)
            return redirect('/')
        return render(request, 'create.html', {'form' : form,})

        def get(self, request, *args, **kwargs):
            form = UserCreationForm(request.POST)
            return render(request, 'create.html', {'form' : form})
    


