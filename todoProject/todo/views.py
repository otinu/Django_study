from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TodoModel

from django.urls import reverse_lazy

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate') # form.〇〇でどのフィールドを使うのか指定する
    success_url = reverse_lazy('list') # urls.pyの別名(path()の第三引数)を指定